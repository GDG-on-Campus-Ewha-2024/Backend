from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

class Blog(models.Model):
    title=models.CharField(max_length=200, null=False, blank=False)
    body=models.TextField(null=False, blank=False)
    date=models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not self.title:
            raise ValidationError('제목을 입력해 주세요.')
        if not self.body:
            raise ValidationError('본문을 입력해 주세요.')

    def __str__(self):
        return self.title

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField("별명", max_length=20, null=True, blank=True)
    phone_num = models.CharField("전화번호", max_length=20, null=True, blank=True)


    class Meta:
        db_table = "user"