from django.urls import path
from . import views

app_name='pybo'

# path('<int:usermodel_id>/', views.detail),
# : url의 int가 usermodel_id 라는 변수명으로 view에서 사용
# name=' ' : URL 별칭
urlpatterns=[
  path('', views.index, name='index'),
  path('<int:question_id>/', views.detail, name='detail'),
  path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
  path('question/create/', views.question_create, name='question_create'),
]