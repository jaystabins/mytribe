from django.db import models
from users.models import User
from posts.models import Post
from django.contrib.humanize.templatetags import humanize
from django.urls import reverse_lazy


# TODO Expand on Manager, clean up queries for nested comments
# Currently tied to main post list and commment component
class CommentManager(models.Manager):
    def all(self):
        qs = super(CommentManager, self).filter(parent=None)
        return qs


class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    parent = models.ForeignKey("self", blank=True, null=True, related_name="children", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def get_date(self):
        return humanize.naturaltime(self.created_at)

    def children(self):  # replies
        return Comment.objects.filter(self=self)

    def __str__(self):
        return self.content

    def hasChildren(self):
        if Comment.objects.filter(parent_id=self):
            return True
        return False

    def isParent(self):
        if self.parent is not None:
            return False
        return True
