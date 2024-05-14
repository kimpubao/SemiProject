from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('<int:news_id>/', views.detail),
]