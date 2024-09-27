from django.contrib import admin
from django.urls import path
from myApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Index 페이지
    path('new_post/', views.new, name="new_post"),  # 새 글 작성 페이지
    path('create/', views.create, name="create"),  # 글 생성 처리
    path('home/', views.home, name="home"),  # 홈 페이지
]
