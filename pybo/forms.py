from django import forms
from .models import Question, Answer
# 장고 웹프레임워크에서는 일반폼과 모델폼(ex.Question모델과 작성한 데이터를 연결하여 저장)을 제공
# 모델폼을 이용하여 질문 모델(Question)과 질문 작성글을 연결하여 db에 저장

class QuestionForm(forms.ModelForm): # 모델폼
    class Meta: # 모델폼을 생성하면 반드시 필요한 클래스임
        model = Question
        fields = ['subject', 'content'] # QuestionForm 모델폼에서 사용할 Question 모델의 속성
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
        labels = {
            'subject': '제목',
            'content': '내용',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }