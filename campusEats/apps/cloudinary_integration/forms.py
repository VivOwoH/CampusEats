from django import forms

# Defining a form for uploading images
class ImageUploadForm(forms.Form):
    # Specifying a field for uploading an image
    image = forms.ImageField()
