from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=256, blank=True)
    phone_num = models.CharField(max_length=15, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='profile_images/', default='default.png', blank=True)
    
    class Meta:
        db_table = "my_user"