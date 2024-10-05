# myApp/urls.py 
from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.post_list, name='post_list'), # 게시물 리스트 조회 
    path('posts/new', views.new, name = 'post_new'), # 새 게시물 작성 폼 
    path('posts/create/', views.post_create, name='post_create'), # 새 게시물 생성 
]