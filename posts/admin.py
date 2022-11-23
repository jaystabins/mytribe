from django.contrib import admin
from posts.models import Post
from comments.models import Comment, Post

admin.site.register(Comment)
# admin.site.register(Like)
admin.site.register(Post)
