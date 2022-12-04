from django.db import models
from users.models import User

# Create your models here.
class Group(models.Model):
    name = models.CharField()
    description = models.CharField()
    is_public = models.BooleanField()
    member = models.ManyToManyField(User, on_delete=models.CASCADE, related_name='members')
    date_created = models.DateTimeField(auto_now_add=True)



class GroupCaravan(Group):
    is_traveling = models.BooleanField()
    region = models.CharField()
    current_loacation = models.CharField()
