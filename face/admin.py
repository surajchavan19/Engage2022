from django.contrib import admin
from .models import *
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=['id', 'created_at','first_name','last_name','temperature_preference']
    search_fields=['id','first_name','last_name','temperature_preference']

admin.site.register(UserOfApp,UserAdmin)

# Django default admin panel
