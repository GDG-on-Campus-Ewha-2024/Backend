from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 메인 페이지에 대한 요청은 myApp의 urls.py로 전달됨 
    # path('', include('myApp.urls')), 

]
