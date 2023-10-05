from django.db import models

# Create your models here.

class Restaurant(models.Model):
    RestaurantID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255, null = False)
    Location = models.CharField(max_length=255, null = True)
    Description = models.CharField(max_length=255, null = True)
    ImageURL = models.CharField(max_length=255, null = True)


