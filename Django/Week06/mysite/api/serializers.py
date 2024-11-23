from rest_framework import serializers
from .models import Food

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food  # 직렬화할 모델
        fields = ['food_id', 'food_name', 'calories']  # 필요한 필드만 직렬화
