from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name='common'

urlpatterns=[
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'),name='login'),
    # http://localhost:8000/common/logout/...
    path('logout/',views.logout_view, name='logout'),
    # http://localhost:8000/common/signup/...
    path('signup/', views.signup, name='signup')
]