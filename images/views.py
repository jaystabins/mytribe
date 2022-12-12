from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Image, ImageAlbum
from users.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy


class ImageListView(LoginRequiredMixin, TemplateView):  # ListView needed for pagination?
    model = Image
    template_name = "images/gallery.html"
    paginate_by = 5

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        context["context_user"] = User.objects.get(id=self.kwargs["pk"])
        context["albums"] = ImageAlbum.objects.filter(user=self.kwargs["pk"])

        if "slug" in self.kwargs:
            slug_album = ImageAlbum.objects.get(user=self.kwargs["pk"], slug=self.kwargs["slug"])
            context["images"] = Image.objects.filter(user_id=self.kwargs["pk"], album=slug_album).order_by(
                "-created_at"
            )
        else:
            context["images"] = Image.objects.filter(user_id=context["context_user"]).order_by("-created_at")
        return context


class ImageDetailView(LoginRequiredMixin, DetailView):
    model = Image
    template_name = "images/view_photo.html"


class ImageCreateView(LoginRequiredMixin, CreateView):
    model = Image
    fields = ["album", "image", "description"]
    template_name = "images/add_photo.html"
    context_object_name = "images"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return redirect("image-gallery", self.request.user.id)

    def get_form(self):
        form = super().get_form()
        form.fields["album"].queryset = ImageAlbum.objects.filter(user=self.request.user)
        return form


class ImageDeleteView(LoginRequiredMixin, DeleteView):
    model = Image

    def get_success_url(self):
        return reverse_lazy("image-gallery", self.request.user.id)


class AlbumCreateView(LoginRequiredMixin, CreateView):
    model = ImageAlbum
    template_name = "images/add_photo.html"
    fields = ["name"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        if form.is_valid():
            return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("image-upload")
