'''
from django.shortcuts import render
import requests

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
# 1. 본인의 앱 뷰 URL
url = "http://127.0.0.1:8000/user/signup/"
response = requests.post(url, data={"key": "value"})

# 2. 요청에 필요한 데이터
post_data = {
    "key1": "value1",
    "key2": "value2"
}

# 3. Authorization 헤더에 Access Token 포함
headers = {
    "Authorization": f"Bearer {"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMyMTIyNTM2LCJpYXQiOjE3MzIxMjIyMzYsImp0aSI6IjdmZmI4N2M3NGFkNDRkM2ViZDI1MTgzZGUwMWMxMWZjIiwidXNlcl9pZCI6Mn0.woUq5iVIrlBwheqAOjYwgrLkZvBRhxi2Nw5627GzPVc"}"
}

# 4. POST 요청 보내기
response = requests.post(app_url, data=post_data, headers=headers)

# 5. 결과 확인
if response.status_code == 200:
    print("Request succeeded:", response.json())
else:
    print("Request failed:", response.text)

class SignUpView(APIView):
    def post(self, request):
        key1 = request.data.get('key1')
        key2 = request.data.get('key2')

        if not key1 or not key2:
            return Response({"error": "Missing keys"}, status=status.HTTP_400_BAD_REQUEST)

        # 데이터 처리 로직
        return Response({"message": "Success", "key1": key1, "key2": key2}, status=status.HTTP_200_OK)


import requests

# 1. Access Token 가져오기
auth_url = "http://127.0.0.1:8000/api/token/"
credentials = {
    "username": "test_user",
    "password": "test_password"
}
response = requests.post(auth_url, data=credentials)
tokens = response.json()  # {"access": "ACCESS_TOKEN", "refresh": "REFRESH_TOKEN"}
access_token = tokens.get("access")

# 2. Access Token을 헤더에 넣고 요청 보내기
app_url = "http://127.0.0.1:8000/accounts/"
headers = {
    "Authorization": f"Bearer {"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMyMTIyNTM2LCJpYXQiOjE3MzIxMjIyMzYsImp0aSI6IjdmZmI4N2M3NGFkNDRkM2ViZDI1MTgzZGUwMWMxMWZjIiwidXNlcl9pZCI6Mn0.woUq5iVIrlBwheqAOjYwgrLkZvBRhxi2Nw5627GzPVc"}"
}
post_data = {
    "key1": "value1",
    "key2": "value2"
}
response = requests.post(app_url, headers=headers, data=post_data)
print("Response with Access Token:", response.status_code, response.json())

# 3. Access Token 없이 요청 보내기
response = requests.post(app_url, data=post_data)
print("Response without Access Token:", response.status_code, response.json())


from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "This is a protected endpoint."})
        
        '''
