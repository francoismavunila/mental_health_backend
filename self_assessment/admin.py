# admin.py
from django.contrib import admin
from .models import SelfAssessmentResponse, UserClassification

class SelfAssessmentResponseAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'mood_happy',
        'mood_sad',
        'mood_irritable',
        'mood_joy',
        'stress_overwhelmed',
        'stress_physical_symptoms',
        'stress_anxious',
        'stress_relax',
        'productivity_productive',
        'productivity_procrastination',
        'productivity_satisfaction',
        'productivity_time_management',
        'self_improvement_goals',
        'self_improvement_learning',
        'self_improvement_reflection',
        'self_improvement_challenge',
        'created_at',
    )

class UserClassificationAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'group',
        'tools',
        'created_at',
        'next_suggested_time'
    )

admin.site.register(SelfAssessmentResponse, SelfAssessmentResponseAdmin)
admin.site.register(UserClassification, UserClassificationAdmin)