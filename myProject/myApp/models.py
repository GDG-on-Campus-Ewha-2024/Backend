from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
  # 기본 유저 모델을 상속 받아 커스터마이징 한 모델

  nickname = models.CharField(max_length=256, blank=False, default='', verbose_name="닉네임") 
  birthday = models.DateField(blank=True, null=True, verbose_name="생일")
  phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="전화번호")
  profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True, verbose_name="프로필 이미지")
  class Meta:
    db_table="my_user"

class Post(models.Model):
  """블로그 게시글 모델"""
  title = models.CharField(max_length=200) # 제목
  content = models.TextField() # 내용
  def __str__(self):
    return self.title  # 관리자 페이지나 Django 쉘에서 Post 객체를 볼 때 제목을 표시