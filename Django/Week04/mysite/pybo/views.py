from django.shortcuts import get_object_or_404,render, redirect
from django.http import HttpResponse
from .models import Question
from django.utils import timezone
from .forms import QuestionForm
from django.core.paginator import Paginator #페이징 기능을 위해

# Create your views here.
def index(request):
  """pybp 목록 출력"""
  #입력 인자
  page=request.GET.get('page','1') #페이지
  #조회
  question_list=Question.objects.order_by('-create_date')
  #페이징 처리
  paginator=Paginator(question_list, 10) #페이징당 10개씩 보여주기
  page_obj=paginator.get_page(page)
  
  context={'question_list': page_obj}
  return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
  """pybo 내용 출력"""
  question=get_object_or_404(Question, pk=question_id)
  context={'question': question}
  return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
  """pybo 답변 등록"""
  question=get_object_or_404(Question, pk=question_id)
  question.answer_set.create(content=request.POST.get('content'),create_date=timezone.now())
  return redirect('pybo:detail', question_id=question.id) #redirect: 함수에 전달된 값을 참고하여 페이지 이동을 수행한다. 첫번째 인수: 이동할 페이지의 별칭, 두번째 인수: 헤당 URL에 전달해야 하는 값

def question_create(request):
  """pybo 질문 등록"""
  if request.method=='POST':
    form=QuestionForm(request.POST)
    if form.is_valid():
      question=form.save(commit=False) #commit=False는 임시저장을 의미
      question.create_date=timezone.now()
      question.save()
      return redirect('pybo:index')
  else: #request.method가 'GET'인 경우 호출!
    form=QuestionForm()
  context={'form': form}
  return render(request, 'pybo/question_form.html', context)