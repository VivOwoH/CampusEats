from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Restaurant(models.Model):
    RestaurantID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255, null = False)
    Location = models.CharField(max_length=255, null = True)
    Description = models.CharField(max_length=255, null = True)
    ImageURL = models.CharField(max_length=255, null = True)
    Rating = models.FloatField(
        validators=[MinValueValidator(1.0), MaxValueValidator(5.0)],
        null=True,
        blank=True
    )


def get_all_restaurants():
    restaurants = Restaurant.objects.all()
    # Create a list to store individual restaurant data
    restaurant_list = []
    
    # Loop through each restaurant object in the queryset
    for restaurant in restaurants:
        restaurant_data = {
            'RestaurantID': restaurant.RestaurantID,
            'Name': restaurant.Name,
            'Location': restaurant.Location,
            'Description': restaurant.Description,
            'ImageURL': restaurant.ImageURL,
            'Rating': restaurant.Rating,
        }
        # Append the individual restaurant data to the list
        restaurant_list.append(restaurant_data)
    
    return restaurant_list
