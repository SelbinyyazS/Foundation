# users/apps.py

from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    # ADD THE 'ready' METHOD BELOW
    def ready(self):
        """
        This method is called when the app is ready.
        We're using it to run our superuser creation script.
        """
        try:
            import os
            from django.contrib.auth import get_user_model

            User = get_user_model()

            # Check if there are any users in the database
            if not User.objects.exists():
                # Get credentials from environment variables
                username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
                email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
                password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

                if username and email and password:
                    print('Creating superuser...')
                    User.objects.create_superuser(
                        username=username,
                        email=email,
                        password=password
                    )
                    print('Superuser created.')
                else:
                    print('Superuser credentials not found in environment variables. Skipping creation.')

        except Exception as e:
            # This helps to see any errors during startup
            print(f"An exception occurred during superuser creation: {e}")