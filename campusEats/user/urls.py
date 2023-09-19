# user/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns for user-related views
    path('user/', views.user_login, name='login'),
]
