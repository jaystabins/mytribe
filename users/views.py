from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView, UpdateView, RedirectView
from django.shortcuts import get_object_or_404
from .models import User, FriendList, FriendRequest
from posts.models import Post
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class UserDetailView(DetailView):
    template_name = "users/user_profile.html"

    def get_queryset(self):
        self.user = get_object_or_404(User, id=self.kwargs["pk"])
        return User.objects.filter(id=self.user.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_data"] = self.user
        context["sender_data"] = User.objects.get(id=self.request.user.id)
        context["posts"] = Post.objects.filter(user_id=self.user.id).order_by("-created_at")
        context["friend_list"] = FriendList.objects.get(user=self.user)
        context["friend_requests"] = FriendRequest.objects.filter(reciever_id=self.user.id, is_active=True)
        context["friend_request_sent"] = FriendRequest.objects.filter(
            reciever_id=self.user.id, sender_id=self.request.user.id
        ).exists()
        context["have_pending_request"] = FriendRequest.objects.filter(
            reciever_id=self.request.user.id, sender_id=self.user.id, is_active=True
        ).exists()
        context["friend_requests_pending"] = FriendRequest.objects.filter(sender_id=self.user.id, is_active=True)
        return context


class UserEditView(UpdateView, LoginRequiredMixin):
    model = User
    template_name = "users/user_edit.html"
    form_class = UserForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy("user", kwargs={"pk": self.object.pk})


class FriendRequestSend(LoginRequiredMixin, RedirectView):
    permanent = False
    query_string = True
    pattern_name = "user"

    def get_redirect_url(self, *args, **kwargs):
        reciever_user = User.objects.get(id=self.kwargs["pk"])
        FriendRequest.objects.get_or_create(sender=self.request.user, reciever=reciever_user)
        return super().get_redirect_url(*args, **kwargs)


# HERE
class FriendRequestAccept(LoginRequiredMixin, RedirectView):
    permanent = False
    pattern_name = "user"

    def get_redirect_url(self, *args, **kwargs):
        request_row = User.objects.get(id=self.kwargs["pk"])
        FriendRequest.objects.get(id=request_row.id).accept()
        return super().get_redirect_url(self.kwargs["return"])


class FriendRequestDecline(LoginRequiredMixin, RedirectView):
    permanent = False
    pattern_name = "user"

    def get_redirect_url(self, *args, **kwargs):
        request_row = User.objects.get(id=self.kwargs["pk"])
        FriendRequest.objects.get(id=request_row.id).decline()
        return super().get_redirect_url(self.kwargs["return"])


class FriendRequestCancel(LoginRequiredMixin, RedirectView):
    permanent = False
    pattern_name = "user"

    def get_redirect_url(self, *args, **kwargs):
        request_row = User.objects.get(id=self.kwargs["pk"])
        FriendRequest.objects.get(id=request_row.id).cancel()
        return super().get_redirect_url(self.kwargs["return"])


class FriendRemove(LoginRequiredMixin, RedirectView):
    pass


class FriendUnfriend(LoginRequiredMixin, RedirectView):
    pass


class FriendAdd(LoginRequiredMixin, RedirectView):
    pass
