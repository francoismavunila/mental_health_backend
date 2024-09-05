from rest_framework import serializers
from .models import Affirmation

class AffirmationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Affirmation
        fields = ['id','user', 'affirmation_text','completed_at']
        read_only_fields = ['user','completed_at']
        