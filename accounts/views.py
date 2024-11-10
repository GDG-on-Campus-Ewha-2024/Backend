from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import CustomUser 
from .forms import CustomUserCreationForm

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

