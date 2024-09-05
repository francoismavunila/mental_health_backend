from django.utils import timezone  # Correct import for Django's timezone utility
from datetime import timedelta  # Import timedelta for date manipulation
from django.db import models
from django.conf import settings

class SelfAssessmentResponse(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mood_happy = models.CharField(max_length=50)
    mood_sad = models.CharField(max_length=50)
    mood_irritable = models.CharField(max_length=50)
    mood_joy = models.CharField(max_length=50)
    stress_overwhelmed = models.CharField(max_length=50)
    stress_physical_symptoms = models.CharField(max_length=50)
    stress_anxious = models.CharField(max_length=50)
    stress_relax = models.CharField(max_length=50)
    productivity_productive = models.CharField(max_length=50)
    productivity_procrastination = models.CharField(max_length=50)
    productivity_satisfaction = models.CharField(max_length=50)
    productivity_time_management = models.CharField(max_length=50)
    self_improvement_goals = models.CharField(max_length=50)
    self_improvement_learning = models.CharField(max_length=50)
    self_improvement_reflection = models.CharField(max_length=50)
    self_improvement_challenge = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

def two_weeks_from_now():
    return timezone.now() + timedelta(weeks=2)
    
class UserClassification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    group = models.CharField(max_length=100)
    tools = models.JSONField()  # Assuming tools is a list of suggested tools
    next_suggested_time = models.DateTimeField(default=two_weeks_from_now)  # Field for the next suggested time
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user.email} - {self.group}"
    
