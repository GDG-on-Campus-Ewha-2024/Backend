from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Blog
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'home_page.html')

def index(request):
    posts_list = Blog.objects.all().order_by('-date')  # 모든 포스트를 가져옵니다.
    paginator = Paginator(posts_list, 5)  # 페이지당 5개의 포스트
    page_number = request.GET.get('page')  # 요청된 페이지 번호
    posts = paginator.get_page(page_number)  # 해당 페이지의 포스트 가져오기

    return render(request, 'index.html', {'posts': posts})

def delete(request, id):
    if request.method == 'POST':
        post = get_object_or_404(Blog, id=id)
        post.delete()
        return HttpResponse(status=200)  # 성공 시 HTTP 200 응답
    return HttpResponse(status=405)  # POST 요청이 아닐 경우 405 응답

def new(request):
    return render(request, 'new_post.html')

def create(request):
    if request.method == 'POST':
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST.get('body')
        post.date = timezone.now()
        try:
            post.clean()  # 유효성 검사 호출
            post.save()    # 저장
            return redirect('index')  # 글 목록 페이지로 리디렉션
        except ValidationError as e:
            return render(request, 'index.html', {'form': post, 'errors': e.messages})
    
    return redirect('index', post.id)  

def edit_post(request, post_id):
    post = get_object_or_404(Blog, id=post_id)  # 해당 포스트 가져오기
    return render(request, 'edit_post.html', {'post': post})

def update(request, post_id):
    post = get_object_or_404(Blog, id=post_id)  # 해당 포스트 가져오기
    if request.method == 'POST':
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        try:
            post.clean()  # 유효성 검사 호출
            post.save()  # 수정된 데이터 저장
            return redirect('index')  # 글 목록 페이지로 리디렉션
        except ValidationError as e:
            return render(request, 'edit_post.html', {'post': post, 'errors': e.messages})
    return redirect('index')  # POST가 아닌 경우에는 홈으로 리디렉션

