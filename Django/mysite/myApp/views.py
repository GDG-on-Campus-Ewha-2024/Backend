from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from .models import UserModel
from django.urls import reverse

# Create your views here.
def hello(request):
  return HttpResponse("안녕하세요!")

def username(request):
  """myApp 목록 출력"""
  usermodel_list=UserModel.objects.order_by('-schoolId')
  context={'user_list':usermodel_list}
  return render(request, 'myApp/username_list.html', context)

def detail(request, usermodel_id):
  """myApp 내용 출력"""
  #첫번째: 클래스, 두번째: pk 값을 가져온다
  usermodel_detail=get_object_or_404(UserModel, pk=usermodel_id)
  return render(request, 'myApp/detail.html', {'usermodel':usermodel_detail})

def home(request):
  return redirect('hello')
