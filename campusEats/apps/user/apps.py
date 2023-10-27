from django.apps import AppConfig

# Configuration for the 'user' app.

class UserConfig(AppConfig):
    # Defining the default auto field for models in this app.
    default_auto_field = 'django.db.models.BigAutoField'

    # Specifying the name of the app, which is 'apps.user'.
    name = 'apps.user'
