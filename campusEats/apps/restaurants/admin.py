# Importing the necessary module for setting up the Django admin
from django.contrib import admin

# Importing the model(s) that we want to make available in the admin interface
from .models import Restaurant

# Registering the model with the admin site
admin.site.register(Restaurant)
