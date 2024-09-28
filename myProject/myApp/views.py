from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.all() # 모든 게시글을 가져옴 
    return render(request, 'post_list.html', {'posts':posts})
