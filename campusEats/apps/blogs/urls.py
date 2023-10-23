from django.urls import path
from . import views

urlpatterns = [
    path('blogs/test/', views.blog_test, name='blog_test')
]