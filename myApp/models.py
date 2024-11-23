from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser,Group, Permission

# Create your models here.
class UserModel(AbstractUser):
    """일반 사용자 커스터마이징"""
    class Meta:
        db_table = "my_user"
        
    nickname = models.CharField(max_length=256, default='')
    birthday = models.DateField(blank=True, null=True)
    
     # 충돌 방지용 related_name 설정
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups1",  # 새로운 이름 설정
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions1",  # 새로운 이름 설정
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )
    