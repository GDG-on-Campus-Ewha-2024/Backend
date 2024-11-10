from django.urls import path
from . import views 

urlpatterns = [
    path('', views.post_list, name='post_list'),     # read : 게시글 목록 
    path('<int:post_id>/', views.post_detail, name='post_detail'),  # read : 게시글 상세 
    path('create/', views.post_create, name='post_create'), # create: 새 게시글 작성 
    path('<int:post_id>/edit/', views.post_edit, name='post_edit'),  # update : 게시글 수정 
    path('<int:post_id>/delete/', views.post_delete, name='post_delete'), # delete : 게시글 삭제
]