# content/models.py

from django.db import models
from django.conf import settings # A way to get the User model you defined in settings.py

class Content(models.Model):
    """
    Represents a piece of learning material uploaded by a user.
    """
    # Let's define the types of content we can have.
    # This uses Django's built-in choices feature.
    class ContentType(models.TextChoices):
        VIDEO = 'VIDEO', 'Video'
        PDF = 'PDF', 'PDF Document'
        IMAGE = 'IMAGE', 'Image'
        TEXT = 'TEXT', 'Text Post'
        PPT = 'PPT', 'Presentation'
        # We can add more later, like 'AUDIO', 'QUIZ', etc.

    # --- Main Fields ---
    title = models.CharField(max_length=200, help_text="The title of the learning material.")
    description = models.TextField(blank=True, help_text="A brief description of the content.")
    
    content_type = models.CharField(
        max_length=10,
        choices=ContentType.choices,
        default=ContentType.TEXT,
        help_text="The format of the content."
    )
    
    # The actual file. 'upload_to' specifies the sub-directory within our media folder.
    # 'blank=True, null=True' makes this field optional, for text-only posts.
    file = models.FileField(upload_to='content_files/', blank=True, null=True)
    
    # --- Timestamps ---
    # auto_now_add=True automatically sets the timestamp when the object is first created.
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now=True automatically updates the timestamp every time the object is saved.
    updated_at = models.DateTimeField(auto_now=True)

    # --- Relationships (The "Who") ---
    # This is a Foreign Key. It links this Content object to a User object.
    # 'settings.AUTH_USER_MODEL' is the proper way to refer to your CustomUser model.
    # 'on_delete=models.CASCADE' means if a user is deleted, all their content is also deleted.
    # 'related_name' lets us easily get all content for a user, e.g., user.content_posts.
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='content_posts'
    )

    def __str__(self):
        """
        A human-readable representation of the model instance,
        which is very useful in the Django admin site.
        """
        return f"{self.title} by {self.creator.username}"