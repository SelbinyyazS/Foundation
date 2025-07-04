# content/views.py

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin # Import this!

from .models import Content
from .forms import ContentForm

# --- Homepage View (already here) ---
def home_view(request):
    # We'll update this later to show the content
    all_content = Content.objects.all().order_by('-created_at') # Get all content, newest first
    context = {
        'content_list': all_content
    }
    return render(request, 'home.html', context)

# --- Content Upload View (NEW) ---
class ContentCreateView(LoginRequiredMixin, CreateView):
    model = Content
    form_class = ContentForm
    template_name = 'content_upload.html' # We will create this template
    success_url = reverse_lazy('home') # Redirect to homepage on success

    def form_valid(self, form):
        """This method is called when valid form data has been POSTed."""
        # We are overriding this method to set the creator to the current user.
        form.instance.creator = self.request.user
        return super().form_valid(form)