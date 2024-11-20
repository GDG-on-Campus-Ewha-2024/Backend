from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('getTrip/', views.TripView.as_view(), name='get_trip'),
    path('bookmark/<int:trip_id>/', views.BookMarkView.as_view(), name='bookmark_trip'),
]