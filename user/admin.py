# admin.py
from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'id',  # Assuming 'id' is a field in CustomUser
        'email',
        'first_name',
        'last_name',
        'is_staff',
        'is_active',
        'date_joined',
    )

admin.site.register(CustomUser, CustomUserAdmin)