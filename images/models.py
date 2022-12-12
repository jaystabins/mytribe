from django.db import models
from django.urls import reverse
from users.models import User
from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save
from django.conf import settings
from django.template.defaultfilters import slugify


class ImageAlbum(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True, max_length=100)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("name", "user")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album = models.ForeignKey(ImageAlbum, null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ImageField(null=False, blank=False)
    is_user_profile = models.BooleanField(default=False)
    is_user_cover = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse("image-detail", kwargs={"pk": self.pk})


@receiver(post_delete, sender=Image)
def delete_image_file(sender, instance, **kwargs):
    if instance.is_user_profile:
        user = User.objects.get(id=instance.user.id)
        user.profile_pic = settings.PLACEHOLDER_PROFILE_IMAGE
        user.save()

    # Clean up Album if all files in the album are deleted
    if instance.album is not None:
        if Image.objects.filter(album=instance.album.id, user=instance.user).count() == 0:
            ImageAlbum.objects.get(id=instance.album.id, user=instance.user).delete()

    instance.image.delete(False)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_image(sender, instance, created, **kwargs):
    if not created:
        # get Profile Pic Album
        album, created = ImageAlbum.objects.get_or_create(name="Profile Pictures", user=instance)

        if instance.profile_pic != settings.PLACEHOLDER_PROFILE_IMAGE:

            # Query to find if there is a current profile picture set for the user
            try:
                img1 = Image.objects.get(user=instance.id, is_user_profile=True)
                # Check if the current profile pic is the same as the one passed in
                if img1.image == instance.profile_pic:
                    return
                else:
                    img1.is_user_profile = False
                    img1.save()
                    Image.objects.create(user=instance, image=instance.profile_pic, is_user_profile=True, album=album)
            except Image.DoesNotExist:
                Image.objects.create(user=instance, image=instance.profile_pic, is_user_profile=True, album=album)
