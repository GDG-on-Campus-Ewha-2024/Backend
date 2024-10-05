from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .models import Post
from django.core.exceptions import ValidationError # ValidationError import 
from django.utils import timezone # timezone 모듈 import 

def post_list(request):
    posts = Post.objects.all() # Post 모델의 데이터를 가져옴 
    return render(request, 'post_list.html', {'posts':posts}) 

def new(request):
    return render(request, 'new_post.html')

def post_create(request):
    if request.method == 'POST':
        post = Post()
        post.title = request.POST['title'] # POST 요청에서 'title' 데이터를 가져옴 
        post.body = request.POST.get('body') # POST 요청에서 'body' 데이터를 가져옴
        post.date = timezone.now() # 현재 시간을 게시물의 날짜로 저장 

        try: 
            post.clean() # 유효성 검사
            post.save() # 게시물을 데이터베이스에 저장 
            return redirect('post_list') # post_list으로 redirect 
        except ValidationError as e:
            return render(request, 'new_post.html', {'form':post, 'errors':e.message})
    return redirect('post_list', post.id)

