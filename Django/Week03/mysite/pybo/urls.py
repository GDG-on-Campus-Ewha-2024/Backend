from django.urls import path
from . import views

app_name = 'pybo'

urlpatterns = [
    # 질문 목록
    path('', views.index, name='index'),
    
    # 질문 상세
    path('<int:question_id>/', views.detail, name='detail'),
    
    # 질문 생성
    path('create/', views.question_create, name='question_create'),
    
    # 질문 수정
    path('update/<int:question_id>/', views.question_update, name='question_update'),
    
    # 질문 삭제
    path('delete/<int:question_id>/', views.question_delete, name='question_delete'),
]
