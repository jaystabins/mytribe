from django.db import models
from django.contrib.auth.models import BaseUserManager, PermissionsMixin, AbstractBaseUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    def create_user(
        self, email, password=None, is_staff=False, 
        username=None, is_active=True, **extra_fields
    ):
        print(username)
        if not email:
            raise ValueError(_('The Email must be set'))
        if not username:
            raise ValueError(_('You must enter a Username'))
        
        
        email = UserManager.normalize_email(email)

        user = self.model(
            email=email, is_active=is_active, user_name=username, is_staff=is_staff, **extra_fields
        )
        if password:
            user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        return self.create_user(
            email, password, is_staff=True, is_superuser=True, **extra_fields
        )


    def staff(self):
        return self.get_queryset().filter(is_staff=True)

class User(PermissionsMixin, AbstractBaseUser):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    user_name = models.CharField(max_length=30, blank=True, unique=True)
    email = models.EmailField(unique=True, blank=False, null=False)
    gender = models.CharField(max_length=10, blank=True)
    relationship_status = models.CharField(max_length=256, blank=True)
    bio = models.TextField(blank=True)
    current_location = models.CharField(max_length=256, blank=True)
    hometown = models.CharField(max_length=256, blank=True)
    profile_pic = models.CharField(max_length=256, blank=True)
    post_public = models.BooleanField(default=True) 
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    last_login = models.DateTimeField(verbose_name='last login',auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    # ########################
    # Need to add SOCIAL links
    # ########################
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['user_name']
    
    objects = UserManager()
    
    def __str__(self):
        return f"{self.user_name}'s Profile"