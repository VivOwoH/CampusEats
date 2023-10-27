from django import forms
from .models import Blog
from .models import Comment

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['author', 'title', 'content', 'restaurant']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

