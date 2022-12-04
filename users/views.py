from django.shortcuts import render
from django.views.generic import DetailView, FormView
from django.shortcuts import get_object_or_404
from .models import User
from posts.models import Post
from .forms import UserForm

# Create your views here.
class UserDetailView(DetailView):
    template_name = 'users/user_profile.html'

    def get_queryset(self):
        self.user = get_object_or_404(User, id=self.kwargs['pk'])
        return User.objects.filter(id=self.user.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_data'] = self.user
        context['posts'] = Post.objects.filter(user_id=self.user.id).order_by('-created_at')
        return context

class UserEditView(FormView):
    template_name = 'users/user_edit.html'
    form_class = UserForm
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)