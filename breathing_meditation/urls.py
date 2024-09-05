from django.urls import path
from .views import BreathingAndMeditationSettingsView, BreathingAndMeditationEngagementView

urlpatterns = [
    path('tools/breathing-meditation/settings/', BreathingAndMeditationSettingsView.as_view(), name='breathing-meditation-settings'),
    path('tools/breathing-meditation/engagement/', BreathingAndMeditationEngagementView.as_view(), name='breathing-meditation-engagement'),
]
