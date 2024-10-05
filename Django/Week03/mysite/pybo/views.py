from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Question
from django.utils import timezone
from django import forms

# Create your views here.
# 질문 생성 및 수정을 위한 폼
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']

# Create your views here.
def index(request):
    """질문 목록 출력"""
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    """질문 내용 출력"""
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

def question_create(request):
    """질문 등록"""
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

def question_update(request, question_id):
    """질문 수정"""
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

def question_delete(request, question_id):
    """질문 삭제"""
    question = get_object_or_404(Question, pk=question_id)
    question.delete()
    return redirect('pybo:index')