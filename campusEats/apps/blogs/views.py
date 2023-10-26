from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *

from rest_framework import generics
from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer

def blog_test(request):
    return render(request, 'blogs/test.html')


#
# ListCreateAPIView Usage Guide: (the other one works similarly)
#
# 1. Endpoint URL: /articles/
#
# 2. Supported HTTP Methods:
#    - GET: Fetches a list of all articles.
#    - POST: Creates a new article.
#
# 3. POST Request Format:
#    Send a JSON payload with the following structure:
#    {
#        "title": "<Article Title>",
#        "content": "<Article Content>",
#        "restaurant": <Restaurant ID>,
#        "author": <Author/User ID>
#    }
#
# 4. Responses:
#    - For successful article creation: Returns a `201 Created` status with the
#             serialized data of the new article.
#    - For listing articles: Returns a list of serialized articles.
#    - For validation errors during article creation: Returns a `400 Bad Request`
#             status with details of the errors.
#
# Note: Ensure that the provided Restaurant ID and Author/User ID exist in the
#             database before making a POST request.
#


# Article Views

# The ListCreateAPIView does two main things:
# List: When accessed with a GET request, it lists all the articles.
# Create: When accessed with a POST request and provided with appropriate data,
# it creates a new article.

class ArticleListView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

# ArticleDetailView: Inherits from RetrieveUpdateDestroyAPIView.
# Retrieve: With a GET request and an article's ID, it fetches and returns
# that specific article.
# Update: With a PUT or PATCH request, it updates the specified article's data.
# Destroy: With a DELETE request, it deletes the specified article.

class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

# Comment Views
class CommentListView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
