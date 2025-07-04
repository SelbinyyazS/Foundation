# content/urls.py
from django.urls import path
from .views import ContentCreateView

urlpatterns = [
    path('upload/', ContentCreateView.as_view(), name='content_upload'),
]