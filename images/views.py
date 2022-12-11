from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Image, ImageAlbum
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse_lazy


class ImageListView(LoginRequiredMixin, ListView):
    model = Image
    template_name = "images/gallery.html"
    context_object_name = "images"
    paginate_by = 5

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["albums"] = ImageAlbum.objects.filter(user=self.request.user)
        if "pk" in self.kwargs:
            context["images"] = Image.objects.filter(user_id=self.request.user, album=self.kwargs["pk"]).order_by(
                "-created_at"
            )
        else:
            context["images"] = Image.objects.filter(user_id=self.request.user).order_by("-created_at")
        return context


class ImageDetailView(LoginRequiredMixin, DetailView):
    model = Image
    template_name = "images/view_photo.html"

    def get_queryset(self):
        self.user = get_object_or_404(Image, id=self.kwargs["pk"])
        return Image.objects.filter(pk=self.kwargs["pk"])

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["image"] = Image.objects.get(id=self.kwargs["pk"])
        return context


class ImageCreateView(LoginRequiredMixin, CreateView):
    model = Image
    fields = ["album", "image", "description"]
    template_name = "images/add_photo.html"
    context_object_name = "images"

    def form_valid(self, form):
        form.instance.user = self.request.user
        if form.is_valid():
            item = form.save()
            return redirect("image-gallery")


class ImageDeleteView(LoginRequiredMixin, DeleteView):
    model = Image

    def get_success_url(self):
        return reverse_lazy("image-gallery")


class AlbumCreateView(LoginRequiredMixin, CreateView):
    model = ImageAlbum
    template_name = "images/add_photo.html"
    fields = ["name"]

    def form_valid(self, form):
        print("here")
        form.instance.user = self.request.user
        if form.is_valid():
            return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("image-gallery")
