from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myApp/', include('myApp.urls')),  # myApp의 URL 포함
    path('users/', include('users.urls')),  # users의 URL 포함
    path('trip/', include('trip.urls')),
    path('', include('myApp.urls')),  # 기본 URL 패턴 추가
    path('', include('users.urls')),  # 기본 URL 패턴 추가
]
