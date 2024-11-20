from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    # 새로운 필드 선언 가능(커스텀)

    class Meta:
        model = User
        fields = "__all__"
