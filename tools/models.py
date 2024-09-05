from django.db import models
from django.conf import settings
from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

class JournalEntry(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Journal Entry by {self.user.email} on {self.created_at}"
    

class ToolEngagement(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tool_name = models.CharField(max_length=50)
    date = models.DateField(default=timezone.now)
    engaged = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'tool_name', 'date')

    def __str__(self):
        return f"{self.user.email} - {self.tool_name} on {self.date}"

