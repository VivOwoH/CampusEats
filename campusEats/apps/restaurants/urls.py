# user/urls.py
from django.urls import path, include, re_path as url
from . import views

urlpatterns = [
    # Other URL patterns for user-related views
    # path('login/', views.user_login, name='login'),
    path('', views.render_home, name='Home'),
   
]
