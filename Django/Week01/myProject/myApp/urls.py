from django.shortcuts import render, redirect, HttpResponse
from django.urls import path
from . import views


urlpatterns = [
    # path('index/', views.index, name="index"),  # 테스트용 피드페이지 urls
    # path('tmp/', views.tmp, name='tmp'),
    # path('create/', views.create, name='create'),
    # path('read/', views.read, name='read'),
    # path('update/<int:article_id>', views.update, name='update'),
    # path('delete/<int:article_id>', views.delete, name='delete'),
]