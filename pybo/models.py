from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE,null=True, related_name='author_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter=models.ManyToManyField(User, related_name='voter_question') #추천자
    def __str__(self):
        return self.subject

class Answer(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer', null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 위의 질문이 삭제되면 답변도 삭제해라
    content = models.TextField()
    create_date = models.DateTimeField()
    voter=models.ManyToManyField(User, related_name='voter_answer') #추천자
    modify_date = models.DateTimeField(null=True, blank=True)
