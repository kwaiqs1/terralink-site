from django.contrib import admin
from .models import ContactRequest


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'organization', 'product_interest', 'status', 'created_at']
    list_filter = ['status', 'product_interest', 'created_at']
    search_fields = ['name', 'email', 'organization', 'message']
    readonly_fields = ['created_at', 'ip_address']
    ordering = ['-created_at']
    date_hierarchy = 'created_at'

