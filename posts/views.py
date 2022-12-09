from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from posts.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.core import serializers


class PostListVeiw(ListView):
    template_name = "posts/post_list.html"
    model = Post
    context_object_name = "posts"
    paginate_by = 5
    queryset = Post.objects.all().prefetch_related("comments").order_by("-created_at")


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["post"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        if form.is_valid():
            item = form.save()
            return redirect("main-feed")
        #     return JsonResponse({"name": self.request.user.user_name}, status=200)
        # else:
        #     return JsonResponse({"error": form.errors}, status=400)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post

    def get_success_url(self):
        return reverse_lazy("main-feed")
