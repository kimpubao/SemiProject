from django.urls import path
# from . import views
from .views import base_views, question_views, answer_views
app_name = 'pybo'

# urlpatterns = [
#     path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
#     path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
#     path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
#     path('question/modify/<question_id>/', views.question_modify, name='question_modify'),
#     path('', views.index, name='index'),
#     # 'pybo/' + '' => 'pybo/'
#     # 'pybo/' + 'question' => 'pybo/question'
#     # config/urls.py + pybo/urls.py => 최종 url
#     path('<int:question_id>/', base_views.detail, name='detail'),
#     # http://127.0.0.1/pybo/<int:question_id>/
#     path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
#     # http://127.0.0.1/pybo/answer/create/2/
#     # => question_id에 2개 전달됨
#     # 답변 내용은 request 변수에 전달됨
#     path('question/create/', views.question_create, name='question_create')
# ]

# ex) http://127.0.0.1/pybo/question/create

urlpatterns = [
    # base_views.py
    path('',
         base_views.index, name='index'),
    path('<int:question_id>/',
         base_views.detail, name='detail'),

    # question_views.py
    path('question/create/',
         question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/',
         question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/',
         question_views.question_delete, name='question_delete'),
    path('question/vote/<int:question_id>/',
         question_views.question_vote, name='question_vote'),


    # answer_views.py
    path('answer/create/<int:question_id>/',
         answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/',
         answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/',
         answer_views.answer_delete, name='answer_delete'),
    path('answer/vote/<int:answer_id>/',
         answer_views.answer_vote, name='answer_vote'),
]