from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('search/', views.search, name='search'),
    path('<int:news_id>/', views.detail),
    # path('article/<int:pk>/summary/', views.article_summary, name='summary'),
]
