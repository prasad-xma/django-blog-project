from django.db import models
# from accounts.models import User
from django.conf import settings

# Create your models here.
class Blog(models.Model):
    STATUS_CHOICES = (
        ('public', 'Public'),
        ('private', 'Private')
    )
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='public')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blogs')
    owner_name = models.CharField(max_length=150, editable=False)
    tags = models.CharField(max_length=255, blank=True, help_text="Comma-separated tags")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if self.owner:
            self.owner_name = self.owner.get_full_name() or self.owner.username
        super().save(*args, **kwargs)
        
    
    def __str__(self):
        return f"{self.title} - {self.owner_name}"