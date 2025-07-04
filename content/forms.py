# content/forms.py

from django import forms
from .models import Content

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'description', 'content_type', 'file']
        # We don't include 'creator' because we will set that automatically
        # in the view based on the logged-in user.