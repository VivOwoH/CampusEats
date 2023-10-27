from django.apps import AppConfig
from django.conf import settings
import cloudinary

class CloudinaryIntegrationConfig(AppConfig):
    name = 'apps.cloudinary_integration'

    def ready(self):
        cloudinary.config(
            cloud_name='dzkacabp7',
            api_key=settings.CLOUDINARY_API_KEY, 
            api_secret=settings.CLOUDINARY_API_SECRET
        )
