from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField("별명", max_length=20, null=True, blank=True)
    phone_num = models.CharField("전화번호", max_length=20, null=True, blank=True)


    class Meta:
        db_table = "user"