from django.forms import ModelForm
from .models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'email',
            'user_name',
            'password',
            'first_name',
            'last_name',
            'bio',
            'profile_pic',
            'post_public',
            
        ]