from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if username == 'guest' and password == 'guest':
            # 아이디와 비밀번호가 올바르면 로그인 성공 메시지
            return JsonResponse({"message": "로그인 성공"}, status=200)
        else:
            # 잘못된 아이디 또는 비밀번호
            return JsonResponse({"message": "로그인 실패"}, status=400)

    return render(request, 'login.html')
