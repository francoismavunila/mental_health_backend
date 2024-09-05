from rest_framework import serializers
from .models import JournalEntry

class JournalEntrySerializer(serializers.Serializer):
    content = serializers.CharField(max_length = 2000)
    created_at = serializers.DateTimeField(read_only=True)
    
    def create(self, validated_data):
        user = self.context['request'].user
        return JournalEntry.objects.create(user=user, **validated_data)