from django.contrib import admin

# Registering your models here.

# Importing the CustomUser model from the current directory and register it with the admin interface.
from .models import CustomUser

# Registering the CustomUser model so that it's accessible in the Django admin site.
admin.site.register(CustomUser)
