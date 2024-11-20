from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny

# Create your views here.
class SignInView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            email = request.data.get("email")
            password = request.data.get("password")
            user = get_object_or_404(User, email=email)

            return Response({
                "message" : "로그인 성공"
            }, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response({
                "message": "존재하지 않는 회원입니다. 회원가입을 진행해 주세요."
            }, status=status.HTTP_404_NOT_FOUND)
            # or
            # return RedirectResponse("/signup/")
        
class SignUpView(APIView):
    def post(self, request):
        # permission_classes = [AllowAny]  # 인증 없이 접근 가능 - 디폴트 인증 활성화 시 일부 클래스에 적용 가능
        print(request.data)
        email = request.data.get("email")
        username = request.data.get("username")
        password = request.data.get("password")

        User.objects.create_user(email=email, username=username, password=password) # create 을 쓰면 password hash 가 x

        return Response({
            "message": "회원가입 완료"
        }, status=status.HTTP_200_OK)
    
class FollowView(APIView):
    def post(self, request):
        # 마음에 드는 유저 팔로우
        pass



        
