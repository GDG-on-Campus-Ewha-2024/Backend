from django.contrib import admin
from django.urls import path, include
from users import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),  # signup 페이지
    path('login/', views.login_view, name='login'),  # login 페이지 추가
    path('logout/', views.logout, name='logout'),  # 로그아웃 URL
    path('', include('allauth.urls')),
]
