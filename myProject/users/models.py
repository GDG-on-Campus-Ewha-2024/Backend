# myApp/models.py
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile_pics/', default='default.png')

    def __str__(self):
        return self.user.username
