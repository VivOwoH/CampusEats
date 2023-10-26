from django.urls import path
from . import views
from django.urls import path
from .views import *


urlpatterns = [
    path('blogs/test/', views.blog_test, name='blog_test'),
    path('blogs/articles/<int:pk>/', ArticleListOrAdd.as_view(), name='article-list-add'),
    path('blogs/articles/', ArticleGetEditDel.as_view(), name='article-get-edit-del'),
    path('blogs/articles/<int:article_id>/comments/', CommentListOrAdd.as_view(), name='article-list-add'),
    path('blogs/articles/<int:article_id>/comments/<int:pk>/', CommentGetEditDel.as_view(), name='article-get-edit-del'),
]