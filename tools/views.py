from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import JournalEntry, ToolEngagement
from .serializers import JournalEntrySerializer
from django.utils import timezone  # Correct import for Django's timezone utility
from datetime import timedelta  # Import timedelta for date manipulation


class JournalEntryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        entries = JournalEntry.objects.filter(user=request.user).order_by('-created_at')
        serializers = JournalEntrySerializer(entries, many=True)
        return Response(serializers.data)
    
    def post(self, request):
        serializer = JournalEntrySerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateToolEngagement(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        tool_name = request.data.get('tool_name')
        date = timezone.now().date()

        engagement, created = ToolEngagement.objects.get_or_create(
            user=request.user,
            tool_name=tool_name,
            date=date
        )
        engagement.engaged = True
        engagement.save()

        return Response({'message': 'Engagement updated successfully.'})

class GetDailyEngagement(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        date = timezone.now().date()
        engagements = ToolEngagement.objects.filter(user=request.user, date=date)

        engagement_data = {
            engagement.tool_name: engagement.engaged
            for engagement in engagements
        }

        return Response(engagement_data)