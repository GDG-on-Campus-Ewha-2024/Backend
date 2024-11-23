from django.contrib import admin
from django.urls import path, include
from .views import LoginView,SignUpView
from myApp import views  # views 모듈 임포트
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/profile', include('allauth.urls')),
    path('login/', LoginView, name='login'),
    path('getTrip/', views.get_trip, name='get_trip'),
    path('signup/', SignUpView.as_view(), name='sign_up'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
