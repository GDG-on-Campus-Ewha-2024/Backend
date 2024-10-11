from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Index 페이지
    path('posts/', views.index, name='index'),
    path('new_post/', views.new, name="new_post"),  # 새 글 작성 페이지
    path('create/', views.create, name="create"),  # 글 생성 처리
    path('edit_post/<int:post_id>/', views.edit_post, name="edit_post"),  # 글 수정 페이지
    path('update/<int:post_id>/', views.update, name="update"),  # 글 수정 처리
    path('delete/<int:id>/', views.delete, name='delete'),  # 글 삭제 처리
    path('users/', include('users.urls')),  # users.urls 포함
    

    
]
