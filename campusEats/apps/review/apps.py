from django.apps import AppConfig

# Configuration for the 'review' app
class ReviewConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Setting the default auto field for models
    name = 'apps.review'  # Specifying the name of the 'review' app
