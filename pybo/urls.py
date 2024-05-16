from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('pybo/', views.index, name='pybo'),
    path('search/', views.search, name='search'),
    path('<int:news_id>/', views.detail),
    path('summary/<int:news_id>/<str:content>/', views.summary, name='summary'),
    # path('article/<int:pk>/summary/', views.article_summary, name='summary'),
]
