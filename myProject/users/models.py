from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
from trip.models import Trip

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password, username):
        if not email:
            raise ValueError('must have user email')
        if not password:
            raise ValueError('must have user password')
        
        user = self.model(
            
            email = self.normalize_email(email),
            username=username,
            password=password            
        )
        
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self, email, password, username):
        if not email:
            raise ValueError('must have user email')
        if not password:
            raise ValueError('must have user password')
        
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password
        )
        user.is_admin=True
        user.is_superuser=True
        user.is_active=True
        user.save(using=self.db)
        return user

    def get_by_natural_key(self, email):
        return self.get(email=email)

class User(AbstractBaseUser, PermissionsMixin):
    
    email=models.EmailField(unique=True)
    username=models.CharField(max_length=30, null=True)
    password=models.CharField(max_length=20)
    follow=models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followee')
    place=models.ManyToManyField(Trip, related_name="trip", null=True, blank=True)
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'username']

    objects=UserManager()

    def __str__(self):
        return self.email
    
    @property
    def is_staff(self):
        return self.is_admin