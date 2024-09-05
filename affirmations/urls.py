from django.urls import path
from .views import AffirmationCreateView, AffirmationListView

urlpatterns = [
    path('', AffirmationListView.as_view(), name='affirmation-list'),
    path('new/', AffirmationCreateView.as_view(), name='affirmation-create'),
]
