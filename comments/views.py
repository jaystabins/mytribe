from django.shortcuts import render
from comments.models import Comment
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy

# TODO Need to error check/sanitize this data Check login ect


@login_required
def createComment(request):

    if request.POST.get("parentId"):
        parentId = request.POST.get("parentId")
    else:
        parentId = None

    if request.method == "POST":
        comment = Comment.objects.create(
            user=request.user,
            content=request.POST.get("comment"),
            post_id=request.POST.get("postId"),
            parent_id=parentId,
        )
    return redirect("main-feed")


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment

    def get_success_url(self):
        return reverse_lazy("main-feed")
