from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError


def validate_honeypot(value):
    """Honeypot field validator - should always be empty"""
    if value:
        raise ValidationError('Spam detected')


class ContactRequest(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('read', 'Read'),
        ('replied', 'Replied'),
        ('archived', 'Archived'),
    ]
    
    PRODUCT_INTEREST_CHOICES = [
        ('greenhouse_ai', 'TerraLink Greenhouse AI'),
        ('drone_validator', 'TerraLink Drone Validator'),
        ('both', 'Both'),
        ('general', 'General Inquiry'),
    ]
    
    name = models.CharField(max_length=200)
    email = models.EmailField()
    organization = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    product_interest = models.CharField(max_length=30, choices=PRODUCT_INTEREST_CHOICES, default='general')
    file = models.FileField(upload_to='contact_uploads/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Spam protection fields
    honeypot = models.CharField(max_length=50, blank=True, validators=[validate_honeypot])
    
    # Rate limiting tracking
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['status']),
        ]
    
    def __str__(self):
        return f"Contact from {self.name} - {self.email} ({self.status})"

