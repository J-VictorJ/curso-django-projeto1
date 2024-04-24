from django.apps import AppConfig


class RecipesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recipes'  # it'll be the name to setting, 'stead of full path
