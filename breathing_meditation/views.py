from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BreathingAndMeditationSettings, BreathingAndMeditationEngagement
from .serializers import BreathingAndMeditationSettingsSerializer, BreathingAndMeditationEngagementSerializer

class BreathingAndMeditationSettingsView(APIView):
    def get(self, request):
        try:
            settings = BreathingAndMeditationSettings.objects.get(user=request.user)
            serializer = BreathingAndMeditationSettingsSerializer(settings)
            return Response(serializer.data)
        except BreathingAndMeditationSettings.DoesNotExist:
            return Response({"detail": "Settings not found."}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = BreathingAndMeditationSettingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BreathingAndMeditationEngagementView(APIView):
    def get(self, request):
        engagements = BreathingAndMeditationEngagement.objects.filter(user=request.user)
        serializer = BreathingAndMeditationEngagementSerializer(engagements, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BreathingAndMeditationEngagementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
