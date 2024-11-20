from rest_framework import serializers 
from .models import Trip

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = (
            'title',
            'addr1',
            'addr2',
            'zipcode',
            'img'
        )

        # or
        # fields = '__all__'

