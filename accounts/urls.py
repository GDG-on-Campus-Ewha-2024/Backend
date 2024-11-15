from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    # path('', include('allauth.urls')),
    path('logout/', views.logout_view, name='logout'),
]
