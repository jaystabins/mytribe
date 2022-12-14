from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from posts.views import PostListVeiw, PostCreateView, PostDeleteView
from comments.views import createComment, CommentDeleteView
from users.views import (
    UserDetailView,
    UserEditView,
    FriendRequestSend,
    FriendRequestCancel,
    FriendRequestAccept,
    FriendRequestDecline,
    FriendRemove,
    FriendUnfriend,
)


urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),
    path("", PostListVeiw.as_view(), name="main-feed"),
    path("post/create", PostCreateView.as_view(), name="new-post"),
    path("post/createNewComment/", createComment, name="new-comment"),
    path("comment/<int:pk>/delete", CommentDeleteView.as_view(), name="comment-delete"),
    path("post/<int:pk>/delete", PostDeleteView.as_view(), name="post-delete"),
    path("user/<int:pk>", UserDetailView.as_view(), name="user"),
    path("user/edit", UserEditView.as_view(), name="user-edit"),
    path("user/<int:pk>/sendFriendRequest", FriendRequestSend.as_view(), name="send-friend-request"),
    path("user/<int:sender_id>/CancelFriendRequest/<int:reciever_id>", FriendRequestCancel.as_view(), name="cancel-friend-request"),
    path("user/<int:reciever_id>/AcceptFriendRequest/<int:sender_id>", FriendRequestAccept.as_view(), name="accept-friend-request"),
    path(
        "user/<int:reciever_id>/DeclinelFriendRequest/<int:sender_id>",
        FriendRequestDecline.as_view(),
        name="decline-friend-request",
    ),
    path("user/<int:pk>/FriendRemove", FriendRemove.as_view(), name="friend-remove"),
    path("user/<int:pk>/FriendUnfriend", FriendUnfriend.as_view(), name="friend-unfriend"),
    path("images/", include("images.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
