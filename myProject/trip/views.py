from django.shortcuts import render, redirect
from django.conf import settings
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Trip, Course
import os, requests, dotenv
from django.contrib.auth.decorators import login_required
from django.contrib import messages



dotenv.load_dotenv()
api_key = os.getenv("API_KEY")
# Create your views here.

#@login_required(login_url='/users/login/')
def TripView(request):
    if not request.user.is_authenticated:
        messages.info(request, "로그인이 필요합니다.")
        return redirect('login')
    area_code = request.GET.get('areaCode')
    sigungu_code = request.GET.get('sigunguCode')

    if not area_code or not sigungu_code:
        return render(request, 'search.html', {'error': '지역코드와 시군구코드를 입력하세요.'})

    apiurl = "http://apis.data.go.kr/B551011/KorService1/areaBasedList1"

    params = {        
        "numOfRows": 10,
        "pageNo": 1,
        "MobileOS": "ETC",
        "MobileApp": "AppTest",
        "ServiceKey": api_key,
        "_type": "json",
        "arrange": "A",
        "contentTypeId": 32,
        "areaCode": area_code,
        "sigunguCode": sigungu_code
    }
    
    try:
        # API 요청
        response = requests.get(apiurl, params=params)

        # 상태 코드 확인
        if response.status_code != 200:
            return render(request, 'search.html', {'error': 'API 호출 실패'})

        json_data = response.json().get('response', {}).get('body', {}).get('items', {}).get('item', [])

        if not json_data:
            return render(request, 'search.html', {'error': '검색된 관광지가 없습니다.'})

        # 관광지 리스트 생성
        trip_list = []
        for item in json_data:
            trip_data = {
                "title": item.get("title"),
                "addr1": item.get("addr1"),
                "addr2": item.get("addr2"),
                "zipcode": item.get("zipcode"),
                "img": item.get("firstimage", None)  # 첫 번째 이미지가 있을 경우만 포함
            }
            trip_list.append(trip_data)

        # 검색된 관광지 데이터를 show.html로 전달
        return render(request, 'show.html', {'trips': trip_list})

    except requests.exceptions.RequestException as e:
        return render(request, 'search.html', {'error': f'요청 오류: {e}'})


class BookMarkView(APIView):
    permission_classes = [IsAuthenticated]  # 인증된 사용자만 접근 가능

    def post(self, request):
        # 인증된 사용자 확인
        user = request.user  # `request.user`는 로그인된 사용자
        
        # trip_id 가져오기
        trip_id = request.data.get("trip_id")  # POST 데이터에서 trip_id를 가져옵니다.
        
        # trip_id로 해당 Trip 객체 가져오기
        try:
            trip = Trip.objects.get(id=trip_id)
        except Trip.DoesNotExist:
            return Response({"message": "해당 여행지를 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        
        # 이미 북마크한 여행지인지 확인
        if trip in user.bookmarked_trips.all():
            return Response({"message": "이미 북마크한 여행지입니다."}, status=status.HTTP_400_BAD_REQUEST)
        
        # 여행지 북마크 추가
        user.bookmarked_trips.add(trip)
        return Response({"message": "북마크가 완료되었습니다."}, status=status.HTTP_200_OK)