from django.contrib import admin
from .models import UserModel
from django.contrib.auth.admin import UserAdmin
from .models import Post

# Register your models here.
admin.site.register(UserModel, UserAdmin)
admin.site.register(Post)