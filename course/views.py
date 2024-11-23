from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import TouristSpot
from .serializers import TouristSpotSerializer
import requests
import xmltodict
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# 환경 변수 사용
API_KEY = os.getenv("API_KEY")

@api_view(['GET'])
def view_course(request):
    url = f'http://apis.data.go.kr/B551011/KorService1/locationBasedList1?MobileOS=ETC&MobileApp=MyProject&mapX=126.981611&mapY=37.568477&radius=1000&serviceKey={API_KEY}'
    
    response = requests.get(url)
    if response.status_code == 200:
        data_dict = xmltodict.parse(response.content)
        json_data = data_dict.get('response', {}).get('body', {}).get('items', {}).get('item', [])

        # API 데이터를 데이터베이스에 저장 (중복 방지)
        for item in json_data:
            title = item.get('title', '정보없음')
            addr1 = item.get('addr1', '주소 정보 없음')
            TouristSpot.objects.get_or_create(
                title=title,
                defaults={'addr1': addr1}
            )
    
    # 데이터베이스에서 TouristSpot 객체를 가져와 Serializer로 변환
    spots = TouristSpot.objects.all()
    serializer = TouristSpotSerializer(spots, many=True)

    return Response(serializer.data)
