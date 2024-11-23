from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser
from trip.models import Trip

# Create your models here.
class User(AbstractUser):
    """일반 사용자 커스터마이징"""
    class Meta:
        db_table = "trip_table"
        
    place = models.ManyToManyField(Trip, related_name='trip')