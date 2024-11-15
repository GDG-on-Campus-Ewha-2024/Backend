from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('custom-login/', views.login, name='custom_login'),
    path('', include('allauth.urls')),
    path('logout/', views.logout_view, name='logout'),
]
