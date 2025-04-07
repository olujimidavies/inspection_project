from django.contrib import admin
from config.models import Inspection, Condition

# Register your models with the Django admin site
admin.site.register(Inspection)
admin.site.register(Condition)
