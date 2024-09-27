from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator

from django.utils import timezone

def index(request):
    return render(request, 'index.html')

def new(request):
    return render(request, 'new_post.html')

def create(request):
    if request.method == 'POST':
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST.get('body', '')
        post.date = timezone.now()
        try:
            post.clean()  # 유효성 검사 호출
            post.save()    # 저장
            return redirect('home')  # 글 목록 페이지로 리디렉션
        except ValidationError as e:
            return render(request, 'index.html', {'form': post, 'errors': e.messages})
    
    return redirect('home')  

def home(request):
    posts_list = Blog.objects.all().order_by('-date')  # 모든 포스트를 가져옵니다.
    paginator = Paginator(posts_list, 5)  # 페이지당 5개의 포스트
    page_number = request.GET.get('page')  # 요청된 페이지 번호
    posts = paginator.get_page(page_number)  # 해당 페이지의 포스트 가져오기

    return render(request, 'index.html', {'posts': posts})
