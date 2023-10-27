from django import forms
from .models import Blog
from .models import Comment

# Defining a form for creating and updating blogs
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['author', 'title', 'content', 'restaurant', 'imageURL']

# Defining a form for adding comments to blogs
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
