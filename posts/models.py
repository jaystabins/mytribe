from django.db import models
from users.models import User
from django.urls import reverse_lazy
from django.contrib.humanize.templatetags import humanize


class Post(models.Model):
    post = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    # TODO Implement Image(s) field eventually 
    is_public = models.BooleanField(default=True)
    update_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)

    def get_date(self):
        return humanize.naturaltime(self.postCreated)

    def get_success_url(self):
        return reverse_lazy('post-list', kwargs={'pk': self.object.pk})
    
    def __str__(self):
        return self.user
    
    # TODO - This gets called a TON while viewing any feed
    #       Currently needed to link profile to user on post display
    #       Stop Gap till I can clean up user creation with images breaking
    #       profile table
    def get_user_profile_id(self):
        profile = User.objects.get(user_id = self.user.id)
        return profile.id
