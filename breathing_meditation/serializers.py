from rest_framework import serializers
from breathing_meditation.models import BreathingAndMeditationEngagement, BreathingAndMeditationSettings

class BreathingAndMeditationSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BreathingAndMeditationSettings
        fields = ['session_duration', 'meditation_words']

class BreathingAndMeditationEngagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = BreathingAndMeditationEngagement
        fields = ['date', 'duration', 'completed']