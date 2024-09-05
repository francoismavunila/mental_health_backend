from rest_framework import serializers
from .models import SelfAssessmentResponse, UserClassification

class SelfAssessmentResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelfAssessmentResponse
        fields = '__all__'

class UserClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserClassification
        fields = '__all__'