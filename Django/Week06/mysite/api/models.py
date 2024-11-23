from django.db import models

class Food(models.Model):
    # 음식 데이터 모델
    food_id = models.IntegerField(unique=True)  # 음식 ID (고유 식별자)
    food_name = models.CharField(max_length=255)  # 음식 이름
    calories = models.IntegerField()  # 칼로리 수

    def __str__(self):
        return self.food_name