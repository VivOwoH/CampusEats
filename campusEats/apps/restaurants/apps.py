from django.apps import AppConfig

# Defining a configuration for the 'restaurants' app
class RestaurantsConfig(AppConfig):
    # Specifying the default auto field for model creation
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Setting the name of the app
    name = 'apps.restaurants'
