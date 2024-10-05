from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.all() # Post 모델의 데이터를 가져옴 
    return render(request, 'post_list.html', {'posts':posts}) 
