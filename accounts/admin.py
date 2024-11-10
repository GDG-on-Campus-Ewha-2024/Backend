from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'nickname', 'email', 'phone_number', 'birthday', 'address', 'is_staff', 'is_active']
    search_fields = ['username', 'email', 'nickname']
    list_filter = ['is_staff', 'is_active', 'birthday']
    ordering = ['username']