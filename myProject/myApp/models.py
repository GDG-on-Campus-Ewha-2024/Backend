from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser

# Create your models here.
class UserModel(AbstractUser):
    """일반사용자커스터마이징"""
    class Meta:
      db_table="my_user"

    nickname = models.CharField(max_length=256, default='') 
    birthday = models.DateField(blank=True, null=True)