from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

# 게시글 목록 조회 
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts' : posts})

# 게시글 상세 조회 
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {'post' : post})

# 새 게시글 작성 
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_list')
    else: 
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form' : form})
    
# 게시글 수정 
def post_edit(request, post_id): 
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id = post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form':form})

# 게시글 삭제 
def post_delete(request,  post_id): 
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete() 
        return redirect('post_list')
    
    return render(request, 'blog/post_confirm_delete.html', {'post' : post})
