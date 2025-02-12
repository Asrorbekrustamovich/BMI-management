from django.contrib import admin
from django.apps import apps

# Get all models from the current app
app = apps.get_app_config('app')

# Register each model
for model_name, model in app.models.items():
    admin.site.register(model)