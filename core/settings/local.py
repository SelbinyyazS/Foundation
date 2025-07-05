# core/settings/local.py
from .base import *
from dotenv import load_dotenv

load_dotenv()

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Add whitenoise for local testing if you want, but it's not essential
INSTALLED_APPS.insert(5, 'whitenoise.runserver_nostatic')