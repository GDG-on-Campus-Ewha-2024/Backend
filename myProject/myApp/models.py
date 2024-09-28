from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser

# Create your models here.
class UserModel(AbstractUser):
    """일반사용자커스터마이징"""
    class Meta:
      db_table="my_user"

    nickname = models.CharField(max_length=256, default='') 
    birthday = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, verbose_name="전화번호")

class Post(models.Model):
  """블로그 게시글 모델"""
  title = models.CharField(max_length=200) # 제목
  content = models.TextField() # 내용
  def __str__(self):
    return self.title  # 관리자 페이지나 Django 쉘에서 Post 객체를 볼 때 제목을 표시