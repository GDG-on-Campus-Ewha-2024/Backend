# models.py

from django.db import models
from django.conf import settings

class Course(models.Model):
    title = models.CharField(max_length=200)  # 코스 제목
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 코스를 저장한 사용자
    trips = models.ManyToManyField('Trip', related_name='courses', blank=True)  # 코스에 속하는 여러 Trip들

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

class Trip(models.Model):
    title = models.CharField(max_length=200)  # 여행지 이름
    addr1 = models.CharField(max_length=255)  # 주소 (첫 번째)
    addr2 = models.CharField(max_length=255, blank=True)  # 주소 (두 번째, 선택적)
    zipcode = models.CharField(max_length=10, blank=True)  # 우편번호 (선택적)
    img = models.ImageField(upload_to='trip_images/', null=True, blank=True)  # 이미지 (선택적)
    
    # 관련 관광지의 날씨 정보 (선택적 필드)
    weather_info = models.JSONField(null=True, blank=True)  # JSON 형식으로 날씨 정보 저장 (기상청 API 등에서 받아오는 데이터)
    
    # 사용자와의 관계 (북마크)
    users = models.ManyToManyField('users.User', related_name='bookmarked_trips', blank=True)  # 'bookmarked_trips'라는 역참조 필드
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Trip"
        verbose_name_plural = "Trips"