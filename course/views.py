import requests
import xmltodict
from django.shortcuts import render
from django.conf import settings 
from .models import TouristSpot

API_KEY = settings.API_KEY

def view_course(request):
    url = f'http://apis.data.go.kr/B551011/KorService1/locationBasedList1?MobileOS=ETC&MobileApp=MyProject&mapX=126.981611&mapY=37.568477&radius=1000&serviceKey={API_KEY}'
    
    response=requests.get(url)
    if response.status_code==200:
        data_dict=xmltodict.parse(response.content)
        json_data=data_dict.get('response', {}).get('body', {}).get('items', {}).get('item', [])

        # 필요한 데이터 가공 
        selected_items = []
        for item in json_data:
            title=item.get('title', '정보없음')
            addr1=item.get('addr1', '주소 정보 없음')

            # 데이터베이스에 항목 저장 (중복 방지)
            tourist_spot, created = TouristSpot.objects.get_or_create(
                title=title,
                defaults={'addr1': addr1}
            )

            # 템플릿에 표시할 항목 추가 
            selected_items.append({
                'title':title,
                'addr1':addr1
            })
    else:
        selected_items=[]

    return render(request, 'course/course.html', {'selected_items':selected_items})