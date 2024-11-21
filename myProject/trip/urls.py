# trip/urls.py
from django.urls import path
from . import views

app_name = 'trip'

urlpatterns = [
    path('getTrip/', views.TripView, name='get_trip'),
    path('bookmark/', views.BookMarkView.as_view(), name='bookmark_trip'),  # 수정된 URL
    path('search/', views.TripView, name='search'),
]
