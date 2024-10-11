from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.models import UserProfile  # UserProfile 임포트
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout

def signup(request):
    if request.method == 'POST':
        # 폼에서 전달된 데이터 가져오기
        username = request.POST.get('username')
        nickname = request.POST.get('nickname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        image = request.FILES.get('image', 'default.png')  # 기본 이미지 설정

        # 비밀번호 확인
        if password1 != password2:
            return HttpResponse('Passwords do not match', status=400)

        if len(password1) < 8:
            return HttpResponse('Password must be at least 8 characters long', status=400)

        # 비밀번호 생성
        try:
            # 기본 auth.User 모델을 사용하여 사용자 생성
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password1,  # password1 사용
            )

            # UserProfile 모델을 사용하여 추가 정보 저장
            user_profile = UserProfile.objects.create(
                user=user,
                nickname=nickname,
                image=image,
            )
            user_profile.save()

            # 회원가입 후 로그인 페이지로 리다이렉트
            return redirect('home')
        
        except Exception as e:
            return HttpResponse(f"Error: {str(e)}", status=500)

    elif request.method == 'GET':
        return render(request, 'users/signup.html')
    else:
        return HttpResponse('Invalid request method', status=405)
    
def login_view(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': '유효하지 않은 사용자 이름 또는 비밀번호입니다,'})
    return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':  # POST 요청만 처리
        if request.user.is_authenticated:
            auth_logout(request)
            return redirect('home')
        else:
            return HttpResponse('User not authenticated', status=401)
    else:
        return HttpResponse('Method not allowed', status=405)
