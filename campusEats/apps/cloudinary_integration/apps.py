from django.apps import AppConfig
from django.conf import settings
import cloudinary

# Defining a configuration for Cloudinary integration
class CloudinaryIntegrationConfig(AppConfig):
    # Setting the name of the app
    name = 'apps.cloudinary_integration'

    def ready(self):
        # Configuring Cloudinary with the provided settings
        cloudinary.config(
            cloud_name='dzkacabp7',
            api_key=settings.CLOUDINARY_API_KEY, 
            api_secret=settings.CLOUDINARY_API_SECRET
        )
