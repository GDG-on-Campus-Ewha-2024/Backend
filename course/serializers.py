from rest_framework import serializers 
from .models import TouristSpot

class TouristSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model=TouristSpot
        fields=['title', 'addr1']