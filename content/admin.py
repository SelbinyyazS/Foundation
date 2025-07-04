from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Content # Import the Content model from the same directory

# Register your models here.
admin.site.register(Content)