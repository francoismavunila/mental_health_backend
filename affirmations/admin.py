from django.contrib import admin
from .models import Affirmation

class AffirmationAdmin(admin.ModelAdmin):
    list_display = ('user', 'affirmation_text', 'completed_at')
    search_fields = ('user__email', 'affirmation_text')
    list_filter = ('completed_at',)

admin.site.register(Affirmation, AffirmationAdmin)