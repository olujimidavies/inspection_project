from django.contrib import admin
from config.models import Inspection, Condition

# Registering the models with sql data provided in the Django admin site
admin.site.register(Inspection)
admin.site.register(Condition)
