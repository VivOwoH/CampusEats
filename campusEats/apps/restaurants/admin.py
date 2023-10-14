# In your_app_name/admin.py
from django.contrib import admin
from .models import Restaurant

admin.site.register(Restaurant)
