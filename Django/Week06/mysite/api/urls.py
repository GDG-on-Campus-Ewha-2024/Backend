from django.urls import path
from .views import FoodList

urlpatterns = [
    path('food/', FoodList.as_view(), name='food-list'),
    
]
