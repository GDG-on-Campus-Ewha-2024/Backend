from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import os
from dotenv import load_dotenv
from .serializers import TripSerializer
from user.models import User
from django.shortcuts import get_object_or_404
from .models import Trip
from user.serializers import UserSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

# .env 파일 로드
load_dotenv()

# 환경 변수 가져오기
api_key = os.getenv("API_KEY")


# Create your views here.
@permission_classes([IsAuthenticated]) # class 자체에 접근제한 걸기
class TripView(APIView):
    def post(self, request):
        # 추천 루트를 가져오는 함수

        # 위치 코드
        apiurl = "http://apis.data.go.kr/B551011/KorService1/areaBasedList1"
        params = {
            "serviceKey": api_key,
            "pageNo": 1,
            "numOfRows": 10,
            "MobileApp": "AppTest",
            "MobileOS": "ETC",
            "arrange": "A",
            "contentTypeId": request.data.get("content_type"),
            "areaCode": request.data.get("area_code"),
            "sigunguCode": request.data.get("sigungu"),
            "_type": "json"
        }

        # response = requests.get(apiurl, params=params)
        # or
        request = requests.Request("GET", apiurl, params=params)
        prepared = request.prepare()

        with requests.Session() as session:
            response = session.send(prepared) # 세션으로 http 요청 보냄

        if response.status_code == 200:
            
            json_data = response.json().get('response', {}).get('body', {}).get('items', {}).get('item', [])
            
            for item in json_data:
                # 이미지가 있을 경우
                if item.get("firstimage") != '':
                    
                    serializer = TripSerializer(data={
                        "title": item.get("title"),
                        "addr1": item.get("addr1"),
                        "addr2": item.get("addr2"),
                        "zipcode": item.get("zipcode"),
                        "img": item.get("firstimage")
                    })
                # 이미지가 없을 경우
                else:
                    serializer = TripSerializer(data={
                        "title": item.get("title"),
                        "addr1": item.get("addr1"),
                        "addr2": item.get("addr2"),
                        "zipcode": item.get("zipcode"),
                    })
                # 데이터가 유효하다면
                if serializer.is_valid():
                    serializer.save() 
                else:
                    print(serializer.errors)

            return Response({"message" : "저장 완료"}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class BookMarkView(APIView):
    # 추천 루트를 북마크하는 함수
    def post(self, request, trip_id):
        if request.user.is_authenticated: # post 요청일 경우에만 로그인을 해야 하도록 접근 제한을 걸 수 있다
            # 임의로 유저 가져오기
            user = request.user
            
            place = get_object_or_404(Trip,id=trip_id)
            if place in user.place.all():
                return Response({"message": "이미 있는 장소입니다."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                user.place.add(place)
            return Response({"message" : "저장 완료"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "잘못된 접근"}, status=status.HTTP_400_BAD_REQUEST)

        # or
        # place = Trip.objects.create(
        #     title=request.data.get("title"),
        #     addr1=request.data.get("addr1"),
        #     addr2=request.data.get("addr2"),
        #     zipcode=request.data.get("zipcode"),
        #     user=user
        # )
        # serializer = UserSerializer(user)
        # if serializer.is_valid():
        #     serializer.save(place=place)
        #     return Response({"message" : "저장 완료"}, status=status.HTTP_200_OK)
        # else:
        #     return Response(status=status.HTTP_400_BAD_REQUEST)
            
        
