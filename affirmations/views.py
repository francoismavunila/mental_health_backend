from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Affirmation
from .serializers import AffirmationSerializer

class AffirmationCreateView(generics.CreateAPIView):
    queryset = Affirmation.objects.all()
    serializer_class = AffirmationSerializer
    permission_class = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
        
class AffirmationListView(generics.ListAPIView):
    queryset = Affirmation.objects.all()
    serializer_class = AffirmationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Affirmation.objects.filter(user=self.request.user).order_by('-completed_at')


