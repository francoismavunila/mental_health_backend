from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import CustomUserSerializer, CustomTokenObtainPairSerializer
from django.contrib.auth import login
from .serializers import LoginSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated, AllowAny

class CustomUserCreateView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = CustomTokenObtainPairSerializer

class UserDetailView(APIView):
    
    def get(self, request):
        user = request.user
        print(user)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class HelloView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        return Response({"message": "hello all, cors deployment"}, status=status.HTTP_200_OK)