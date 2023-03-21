from django.contrib import admin
from profiles_api import models

# Register your models so it can show on the admin page
admin.site.register(models.UserProfile)
