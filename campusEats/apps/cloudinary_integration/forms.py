from django import forms

class ImageUploadForm(forms.Form):
    image = forms.ImageField()
    model_name = forms.ChoiceField(
        choices=[('blog', 'Blog'), ('review', 'Review'), ('comment', 'Comment')],
        help_text="Select the model to which you want to associate this image."
    )
    model_id = forms.IntegerField(
        help_text="Enter the ID of the model instance."
    )
