from django.contrib import admin
from .models import JournalEntry, ToolEngagement

@admin.register(JournalEntry)
class JournalEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'content')
    search_fields = ('user__email', 'content')
    list_filter = ('created_at',)

@admin.register(ToolEngagement)
class ToolEngagementAdmin(admin.ModelAdmin):
    list_display = ('user', 'tool_name', 'date', 'engaged')
    search_fields = ('user__email', 'tool_name')
    list_filter = ('date', 'engaged')
    unique_together = ('user', 'tool_name', 'date')