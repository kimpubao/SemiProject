"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from pybo import views
from pybo.views import base_views
urlpatterns = [
    #http://localhost:8000/
    path('', base_views.index, name='index'),
    # path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    #path('pybo/', views.index)
    path('pybo/', include('pybo.urls')), # 기본적으로 request는 여기로 오기 때문에 pybo.urls로 보내는 작업을 진행
    path('common/', include('common.urls'))
    #pybo/q/a, pybo/a/k,...
]