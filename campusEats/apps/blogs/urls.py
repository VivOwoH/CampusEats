from django.urls import path
from . import views
from django.urls import path
from .views import *


urlpatterns = [
    path('blogs/', blog_list_view, name='list_blogs'),
    path('blogs/add/', add_blog_view, name='add_blogs'),
    path('blogs/test/', views.blog_test, name='blog_test'),
    path('blogs/blog/<int:pk>/', BlogListOrAdd.as_view(), name='blog-list-add'),
    path('blogs/blog/', BlogGetEditDel.as_view(), name='blog-get-edit-del'),
    path('blogs/blog/<int:bloge_id>/comments/', CommentListOrAdd.as_view(), name='blog-list-add'),
    path('blogs/blog/<int:blog_id>/comments/<int:pk>/', CommentGetEditDel.as_view(), name='blog-get-edit-del'),
]