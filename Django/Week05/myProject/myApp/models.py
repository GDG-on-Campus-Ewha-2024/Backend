from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser

# Create your models here.
class UserModel(AbstractUser):
  """일반 사용자 커스터마이징"""
  class Meta:
    db_table="my_user"
    
  schoolId=models.IntegerField(default=0)
  major=models.CharField(max_length=256, default='')
