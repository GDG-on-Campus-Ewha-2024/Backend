from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, render
import os
from dotenv import load_dotenv
import requests
from .models import Trip
from .serializers import TripSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# .env 파일 로드
load_dotenv()

# 환경 변수 가져오기
api_key = os.getenv("API_KEY")

class TripView(APIView):
    @csrf_exempt
    def post(self, request):
        
        #위치 코드
        apiurl = "https://apis.data.go.kr/B551011/KorService1/areaBasedList1"
        params = {
            "serviceKey": api_key,
            "pageNo": 1,
            "numOfRows": 10,
            "MobileApp": "AppTest",
            "Mobile05": "ETC",
            "arrange": "A",
            "contentTypeId": request.data.get("content_type"),
            "areaCode": request.data.get("area_code"),
            "sigunguCode": request.data.get("sigungu"),
            "type": "json"
        }
        
        response = requests.get(apiurl,params=params)
        
        if response.status_code == 200:
            json_data = response.json().get('response',{}).get('body',{}).get('items',{}).get('item',{})
            for item in json_data:
                # 이미지가 있을 경우
                if item.get("firstimage") != '':
                    serializer = TripSerializer(data={
                        "title": item.get("title"),
                        "addr1": item.get("addr1"),
                        "addr2": item.get("addr2"),
                        "zipcode": item.get("zipcode"),
                        "img": item.get("firstimage"),
                    })
                # 이미지가 없을 경우
                else:
                    serializer = TripSerializer(data={
                        "title": item.get("title"),
                        "addr1": item.get("addr1"),
                        "addr2": item.get("addr2"),
                        "zipcode": item.get("zipcode"),
                    })
                # 데이터 유효하다면
                if serializer.is_valid():
                    serializer.save()
                else:
                    print(serializer.errors)
                    
            return Response({"message":"저장완료"},status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
# class BookMarkView(APIView):
#     #추천 루트를 북마크하는 함수
#     def post(self, request, trip_id):
#         user = get_object_or_404(User,id=1)
#         place = get_object_or_404(Trip,id=trip_id)
#         if place in user.place.all():
#             return Response({"message": "이미 있는 장소"}, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             user.place.add(place)
#         return Response({"message":"저장완료"},status=status.HTTP_200_OK)