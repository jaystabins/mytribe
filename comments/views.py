from django.shortcuts import render
from django.views.generic import CreateView
from comments.models import Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import redirect


# TODO Need to error check/sanitize this data Check login ect 
def createComment(request):

    if request.POST.get('parentId'):
        parentId = request.POST.get('parentId')
    else:
        parentId = None

    if request.method == 'POST':
        comment = Comment.objects.create(
            user=request.user,
            content=request.POST.get('comment'),
            post_id=request.POST.get('postId'),
            parent_id=parentId,
        )
    return redirect('main-feed')