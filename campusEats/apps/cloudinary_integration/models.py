# Importing necessary Django modules
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Creating a Django model named UploadedImage
class UploadedImage(models.Model):
    # Storing the URL of the uploaded image
    image_url = models.URLField()

    # Capturing the date and time when the image was uploaded
    uploaded_at = models.DateTimeField(auto_now_add=True)
