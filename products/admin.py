from django.contrib import admin
from .models import Product, PricingPlan


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'status', 'order', 'created_at']
    list_filter = ['type', 'status', 'created_at']
    search_fields = ['title', 'short_description', 'long_description']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['order', 'title']


@admin.register(PricingPlan)
class PricingPlanAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price_range_text', 'is_pilot_eligible', 'order']
    list_filter = ['category', 'is_pilot_eligible']
    search_fields = ['name', 'details']
    ordering = ['category', 'order']

