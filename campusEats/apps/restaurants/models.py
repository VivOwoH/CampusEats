from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Restaurant(models.Model):
    RestaurantID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255, null = False)
    Location = models.CharField(max_length=255, null = True)
    Description = models.CharField(max_length=255, null = True)
    ImageURL = models.CharField(max_length=255, null = True)
    Rating = models.DecimalField(
        max_digits=3, decimal_places=2,  # Example values, adjust as needed
        validators=[MinValueValidator(1.0), MaxValueValidator(5.0)],
        null=True, blank=True
    )
    Is_open = models.BooleanField(default=False)
    Open_dates = models.TextField(null=True)
    Phone = models.CharField(max_length=20, null=True)
    PriceLevel = models.IntegerField(null=True, blank=True)
    Takeout = models.BooleanField(default=False)  # Add a field for takeout
    Dine_in = models.BooleanField(default=False)
    Delivery = models.BooleanField(default=False)
    Reservable = models.BooleanField(default=False)
    Serves_vegetarian_food = models.BooleanField(default=False)
    Serves_wine = models.BooleanField(default=False)
    Serves_beer = models.BooleanField(default=False)
    

    def __str__(self):
        return self.Name





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
