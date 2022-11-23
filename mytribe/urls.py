from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from posts.views import PostListVeiw, PostCreateView

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    
    path('', PostListVeiw.as_view(), name='main-feed'),
    path('post/create', PostCreateView.as_view(), name='new-post'),
]
