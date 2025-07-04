

# Register your models here.
# users/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # We are extending the default UserAdmin...
    # For now, we don't need to change much, but we can later.
    # For example, we could add 'bio' to the list_display.
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']

# Unregister the default User admin if it's there, then register our own.
# This is a common pattern, though often not strictly necessary.
admin.site.register(CustomUser, CustomUserAdmin)