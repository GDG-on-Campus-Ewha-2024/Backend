from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='common'

urlpatterns=[
  #별도의 views.py 파일 수정 필요X
  path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
  path('signup/', views.signup, name='signup'),
]