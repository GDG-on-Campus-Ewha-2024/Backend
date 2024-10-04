from django.shortcuts import render, redirect
from .models import myapp

# Create your views here.
def index(request):
    articles = myapp.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'myapp/index.html', context)

def new(request):
    return render(request, 'myapp/new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    article = myapp(title = title, content = content)
    article.save()
    return redirect('/myapp/')

def detail(request, pk):
    article = myapp.objects.get(pk=pk)
    context = {
        'article':article
    }
    return render(request, 'myapp/detail.html', context)

def delete(request, pk):
    article = myapp.objects.get(pk=pk)
    article.delete()
    return redirect('/myapp/')

def edit(request, pk):
    article = myapp.objects.get(pk=pk)
    context = {
        'article':article
    }
    return render(request, 'myapp/edit.html', context)

def update(request, pk):
    article=myapp.objets.get(pk=pk)
    title=request.GET.get('title')
    content=request.GET.get('content')
    article.title=title
    article.content=content
    article.save()
    return redirect(f'/myapp/{article.pk}/')