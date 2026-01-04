from django.contrib import admin
from .models import Pilot


@admin.register(Pilot)
class PilotAdmin(admin.ModelAdmin):
    list_display = ['location', 'country', 'status', 'progress_percent', 'start_date', 'duration_months']
    list_filter = ['status', 'country', 'start_date']
    search_fields = ['location', 'description']
    ordering = ['-start_date']

