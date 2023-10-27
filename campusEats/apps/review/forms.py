from django import forms
from .models import Review

# Define a form for creating or editing reviews
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review  # Using the Review model for the form
        fields = ['RestaurantID', 'Rating', 'Description']  # Specifying the fields to include in the form
