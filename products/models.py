from django.db import models
from django.utils.text import slugify


class Product(models.Model):
    PRODUCT_TYPES = [
        ('ai', 'TerraLink Greenhouse AI'),
        ('drone', 'TerraLink Drone Validator'),
    ]
    
    STATUS_CHOICES = [
        ('concept', 'Concept'),
        ('mvp', 'MVP'),
        ('pilot', 'Pilot'),
        ('production', 'Production'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    short_description = models.TextField(max_length=300)
    long_description = models.TextField()
    type = models.CharField(max_length=20, choices=PRODUCT_TYPES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    features = models.JSONField(default=list, help_text="List of feature strings")
    icon_svg = models.TextField(blank=True, help_text="SVG icon code")
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order', 'title']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title


class PricingPlan(models.Model):
    CATEGORY_CHOICES = [
        ('ai', 'AI Subscription'),
        ('drone', 'Drone Service'),
    ]
    
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price_range_text = models.CharField(max_length=200, help_text="e.g., '450,000 - 3,500,000 KZT / month'")
    monthly_kzt_min = models.IntegerField(help_text="Minimum price in KZT")
    monthly_kzt_max = models.IntegerField(help_text="Maximum price in KZT")
    details = models.TextField(help_text="Pricing details and what's included")
    is_pilot_eligible = models.BooleanField(default=False, help_text="Is this eligible for pilot pricing?")
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['category', 'order', 'monthly_kzt_min']
    
    def __str__(self):
        return f"{self.name} - {self.price_range_text}"

