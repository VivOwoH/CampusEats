from django.db import models

# Create your models here.
from django.contrib.auth.models import User  # Import Django's built-in User model

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Create a one-to-one relationship with User
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)

    def __str__(self):
        return self.user.username
