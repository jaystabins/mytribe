from django.urls import path
from .views import ImageListView, ImageCreateView, ImageDeleteView, ImageDetailView, AlbumCreateView

urlpatterns = [
    path("gallery/<int:pk>", ImageListView.as_view(), name="image-gallery"),
    path("gallery", ImageListView.as_view(), name="image-gallery"),
    path("upload", ImageCreateView.as_view(), name="image-upload"),
    path("create_album", AlbumCreateView.as_view(), name="create-album"),
    path("<int:pk>/delete", ImageDeleteView.as_view(), name="image-delete"),
    path("<int:pk>", ImageDetailView.as_view(), name="image-detail"),
]
