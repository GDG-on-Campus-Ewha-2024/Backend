import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Food
from .serializers import FoodSerializer

import requests, json
from django.http import JsonResponse

from django.conf import settings
API_KEY=settings.API_KEY

class FoodList(APIView):

    def get(self, request):
        # 요청 파라미터 받기
        service_id = request.query_params.get('serviceId', 'COOKRCP01')
        data_type = request.query_params.get('dataType', 'json')
        start_idx = request.query_params.get('startIdx', '16')
        end_idx = request.query_params.get('endIdx', '17')

        # OpenAPI URL 구성 (API_KEY를 f-string을 사용하여 포함)
        url = f'http://openapi.foodsafetykorea.go.kr/api/{API_KEY}/{service_id}/{data_type}/{start_idx}/{end_idx}'
        
        try:
            # API 호출
            response = requests.get(url)
            response.raise_for_status()  # HTTP 오류가 있을 경우 예외 발생

            # 응답 본문 출력 (디버깅용)
            print("Response Status Code:", response.status_code)
            print("Response Text:", response.text)

            # JSON 파싱
            food_data = response.json()  # 응답 JSON 파싱
        except requests.exceptions.RequestException as e:
            return Response({'error': str(e)}, status=500)
        except ValueError:
            return Response({'error': 'Invalid JSON response'}, status=500)

        # 데이터 저장 및 직렬화
        food_list = []
        if 'result' in food_data and 'baseList' in food_data['result']:
            for food_item in food_data['result']['baseList']:
                # 모델에 데이터 저장
                food_instance, created = Food.objects.get_or_create(
                    food_id=food_item['RCP_SEQ'], #일련번호
                    defaults={'food_name': food_item['RCP_NM'], #메뉴명
                            'calories': food_item['INFO_ENG']} #열량
                )
                food_list.append(food_instance)

            # 직렬화된 데이터 반환
            serializer = FoodSerializer(food_list, many=True)
            return Response(serializer.data)
        else:
            return Response({'error': 'No data found'}, status=404)