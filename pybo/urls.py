from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('pybo/', views.index, name='pybo'),
    path('search_dict/', views.search_dict, name='search-dict'),
    path('search_news/', views.search_news, name='search-news'),
    path('<int:news_id>/', views.detail),
    path('summary/<int:news_id>/<str:content>/', views.summary, name='summary'),
    # path('article/<int:pk>/summary/', views.article_summary, name='summary'),
]
