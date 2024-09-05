from django.db import models
from django.conf import settings

class Affirmation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    affirmation_text = models.TextField()
    completed_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.email} - {self.affirmation_text[:50]}"

# Create your models here.
