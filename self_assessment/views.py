from django.utils import timezone  # Correct import for Django's timezone utility
from datetime import timedelta  # Import timedelta for date manipulation
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from tools.models import ToolEngagement
from .models import SelfAssessmentResponse, UserClassification
from .serializers import SelfAssessmentResponseSerializer, UserClassificationSerializer

class GradeUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        data = request.data

        # Save the user's self-assessment response
        data['user'] = user.id
        response_serializer = SelfAssessmentResponseSerializer(data=data)
        if response_serializer.is_valid():
            response_serializer.save()
        else:
            print("res", response_serializer.errors)
            return Response(response_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Classify the user based on their responses
        group = self.classify_user_based_on_responses(data)
        tools = self.suggest_tools_based_on_group(group)
        next_suggested_time = timezone.now() + timedelta(days=7)

        # Save the classification and tools in the database
        classification_data = {
            'user': user.id,
            'group': group,
            'tools': tools,
            'next_suggested_time': next_suggested_time
        }

        classification_serializer = UserClassificationSerializer(data=classification_data)
        if classification_serializer.is_valid():
            classification_serializer.save()
            prepopulate_tool_engagements(user, tools, timezone.now(), next_suggested_time)
            return Response(classification_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(classification_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, *args, **kwargs):
            try:
                # Fetch the latest UserToolGroup entry for the authenticated user
                user_tool_group = UserClassification.objects.filter(user=request.user).latest('created_at')
                
                # Prepare the response data
                data = {
                    'group': user_tool_group.group,
                    'tools': user_tool_group.tools,
                    'next_suggested_time': user_tool_group.next_suggested_time
                }
                return Response(data, status=status.HTTP_200_OK)
            
            except UserClassification.DoesNotExist:
                return Response({"detail": "No assessment found for this user."}, status=status.HTTP_404_NOT_FOUND)

        
        
    def classify_user_based_on_responses(self, responses):
        # Convert string responses to numerical values
        score_map = {
            "never": 1,
            "rarely": 2,
            "sometimes": 3,
            "often": 4,
            "always": 5
        }

        stress_score = (
            score_map[responses.get('stress_overwhelmed')] +
            score_map[responses.get('stress_physical_symptoms')] +
            score_map[responses.get('stress_anxious')] +
            (6 - score_map[responses.get('stress_relax')])  # Inverted score
        )
        mood_score = (
            score_map[responses.get('mood_happy')] +
            (6 - score_map[responses.get('mood_sad')]) +  # Inverted score
            score_map[responses.get('mood_joy')] +
            (6 - score_map[responses.get('mood_irritable')])  # Inverted score
        )
        productivity_score = (
            score_map[responses.get('productivity_productive')] +
            (6 - score_map[responses.get('productivity_procrastination')]) +  # Inverted score
            score_map[responses.get('productivity_satisfaction')] +
            score_map[responses.get('productivity_time_management')]
        )

        # Classify based on scores
        if stress_score >= 15:
            return 'Highly Stressed'
        elif mood_score >= 15 and productivity_score >= 15:
            return 'High Mood and Productivity'
        elif mood_score <= 8:
            return 'Low Mood'
        elif productivity_score <= 8:
            return 'Low Productivity'
        else:
            return 'Balanced'

    def suggest_tools_based_on_group(self, group):
        # Suggest tools based on the user's group classification
        if group == 'Highly Stressed':
            return ['Breathing and Meditation', 'Affirmations', 'Journaling']
        elif group == 'High Mood and Productivity':
            return ['Time Management', 'Goal Setting']
        elif group == 'Low Mood':
            return ['Journaling', 'Positive Quotes', 'Affirmations']
        elif group == 'Low Productivity':
            return ['Time Management', 'Task Prioritization']
        else:
            return ['Journaling', 'Quotes', 'Affirmations']

def prepopulate_tool_engagements(user, tools, start_date, end_date):
    current_date = start_date
    while current_date <= end_date:
        for tool_name in tools:
            ToolEngagement.objects.get_or_create(
                user=user,
                tool_name=tool_name,
                date=current_date,
                defaults={'engaged': False}
            )
        current_date += timedelta(days=1)