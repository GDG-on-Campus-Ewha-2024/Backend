from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser
from django.conf import settings 
from trip.models import Trip


# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password, username):
        if not email:
            raise ValueError("Email is required field")
        
        user = self.model(
            email = self.normalize_email(email),
            password=password,
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, username):
        if not email:
            raise ValueError("Email is required field")
        
        user = self.model(
            email = self.normalize_email(email),
            password=password,
            username=username
        )
        user.set_password(password)

        user.is_admin = True
        user.is_active = True
        
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    username = models.CharField(max_length=50, null=True)
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='followee')
    place = models.ManyToManyField(Trip, related_name="trip", null=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'username']

    def __str__(self):
        return self.email
    
    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True




