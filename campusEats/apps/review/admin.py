from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Review)  # Registering the Review model with the admin
admin.site.register(Reaction)  # Registering the Reaction model with the admin
