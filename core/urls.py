# core/urls.py

from django.contrib import admin
from django.urls import path, include
from content.views import home_view # <-- IMPORT THE VIEW
from django.conf import settings # Import
from django.conf.urls.static import static # Import

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    # Add this line for the content app
    path('content/', include('content.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)