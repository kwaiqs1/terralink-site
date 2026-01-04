from django.contrib import admin
from .models import TeamMember


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'order', 'created_at']
    search_fields = ['name', 'role', 'bio']
    list_filter = ['created_at']
    ordering = ['order', 'name']

