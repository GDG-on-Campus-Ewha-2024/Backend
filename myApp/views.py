# from django.shortcuts import render
# from django.http import JsonResponse
# from django.contrib.auth import authenticate

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)

#         if username == 'guest' and password == 'guest':
#             # 아이디와 비밀번호가 올바르면 로그인 성공 메시지
#             return JsonResponse({"message": "로그인 성공"}, status=200)
#         else:
#             # 잘못된 아이디 또는 비밀번호
#             return JsonResponse({"message": "로그인 실패"}, status=400)

#     return render(request, 'login.html')

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, LoginSerializer

class SignUpView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "회원가입 성공!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

