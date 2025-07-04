# users/views.py

from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    # reverse_lazy is used so it doesn't execute the URL redirect until
    # after the user has been created successfully.
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'