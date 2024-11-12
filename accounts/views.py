from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login 
from .forms import CustomUserCreationForm
from .forms import CustomUserLoginForm

def signup(request): 
    if request.method == 'POST': 
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # 비밀번호를 해싱하여 저장
            user.save()
            return redirect('/login/')
        else: 
            print(form.errors)
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/signup.html', {'form': form})

def login(request): 
    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # 사용자 인증 
            user = authenticate(request, username=username, password=password)

            if user is not None: 
                # 인증된 사용자를 로그인 처리 
                auth_login(request, user)
                return redirect('/home/') # 로그인 후 이동할 페이지
            else: 
                form.add_error(None, "Invalid username or password")
        else:
            print(form.errors)
    else:
        form = CustomUserLoginForm()
    
    return render(request, 'accounts/login.html', {'form': form})

