from django.urls import path
from . import views
from django.urls import path
from .views import *


urlpatterns = [
    path('blogs/test/', views.blog_test, name='blog_test'),
    path('blogs/', views.blog_list, name='list_blogs'),
    path('blogs/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('blogs/add/', views.add_blog, name='add_blog'),
    path('blogs/<int:blog_id>/update/', views.blog_update, name='blog_update'),
    path('blogs/<int:blog_id>/delete/', views.blog_delete, name='blog_delete'),
    path('blogs/<int:blog_id>/comments/', views.blog_comments, name='blog_comments'),
]