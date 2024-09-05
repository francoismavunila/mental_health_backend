from django.db import models
from django.conf import settings

class BreathingAndMeditationSettings(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    session_duration = models.IntegerField(default=5)  # Duration in minutes
    meditation_words = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.email}'s Breathing and Meditation Settings"
    
class BreathingAndMeditationEngagement(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    duration = models.IntegerField()  # Duration engaged in the session in minutes
    completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'date')

    def __str__(self):
        return f"{self.user.email}'s Breathing and Meditation on {self.date}"
