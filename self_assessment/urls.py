from django.urls import path
from .views import GradeUserView

urlpatterns = [
    path('self-assessment-responses/', GradeUserView.as_view(), name='grade-user'),
]
