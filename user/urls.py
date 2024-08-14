# api/urls.py
from django.urls import path
from .views import CustomUserCreateView, LoginView, CustomTokenObtainPairView, UserDetailView

urlpatterns = [
    path('signup/', CustomUserCreateView.as_view(), name='user-create'),
    path('login/', LoginView.as_view(), name='login'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('details/', UserDetailView.as_view(), name='user_details'),
]
