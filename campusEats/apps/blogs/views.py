from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *

from rest_framework import generics
from .models import Blog, Comment
from .serializers import BlogSerializer, CommentSerializer

def blog_test(request):
    return render(request, 'blogs/test.html')

def blog_list_view(request):
    return render(request, 'blogs/list_blogs.html')

def add_blog_view(request):
    return render(request, 'blogs/add_blogs.html')



#
# ListCreateAPIView Usage Guide:
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

class BlogListOrAdd(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

#
# RetrieveUpdateDestroyAPIView Usage Guide:
#
# Endpoint URL: /articles/<ID>/
# Where <ID> is the unique identifier of the Article.
#
# Supported HTTP Methods:
#
# - GET:
#   - Description: Retrieve the details of a specific article.
#   - Payload: None.
#   - Example: `/articles/3/` retrieves the article with ID 3.
#
# - PUT (Full Update):
#   - Description: Update all fields of a specific article.
#   - Payload: JSON object with all article fields.
#   - Example:
#     {
#       "title": "Updated Title",
#       "content": "Updated content...",
#       "restaurant": 2,
#       "author": 4
#     }
#   - Usage: Sending to `/articles/3/` updates the entire article with ID 3.
#
# - PATCH (Partial Update):
#   - Description: Update specific fields of an article.
#   - Payload: JSON object with only fields to update.
#   - Example:
#     {
#       "title": "New Title Only"
#     }
#   - Usage: Sending to `/articles/3/` updates just the title of the article with ID 3.
#
# - DELETE:
#   - Description: Delete a specific article.
#   - Payload: None.
#   - Usage: Sending to `/articles/3/` deletes the article with ID 3.
#
# For PUT and PATCH, ensure the Content-Type header is set to 'application/json'.
#


# RetrieveUpdateDestroyAPIView does these:
# Retrieve: With a GET request and an article's ID, it fetches and returns
# that specific article.
# Update: With a PUT or PATCH request, it updates the specified article's data.
# Destroy: With a DELETE request, it deletes the specified article.

class BlogGetEditDel(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

# Comment Views
class CommentListOrAdd(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    def get_queryset(self):
        # Get the 'article_id' from the URL parameters
        blog_id = self.kwargs['Blog_id']
        # Filter comments based on the given article_id
        return Comment.objects.filter(Blog__id=article_id)


class CommentGetEditDel(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    def get_queryset(self):
        # Get the 'article_id' from the URL parameters
        blog_id = self.kwargs['Blog_id']
        # Filter comments based on the given article_id
        return Comment.objects.filter(Blog__id=article_id)

