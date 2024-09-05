from django.urls import path
from .views import JournalEntryView, GetDailyEngagement, UpdateToolEngagement

urlpatterns = [
    path('journal/', JournalEntryView.as_view(), name='journal-entry'),
    path('engangement/', UpdateToolEngagement.as_view(), name='engagements-update'),
    path('daily/', GetDailyEngagement.as_view(), name='engagements-get'),
]
