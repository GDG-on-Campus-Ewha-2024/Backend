from django.urls import path

from . import views

urlpatterns = [
  path('',views.username),
  path('hello/', views.hello, name='hello'),
  path('<int:usermodel_id>/', views.detail, name='detail'),
  path('home/', views.home, name='home')
]