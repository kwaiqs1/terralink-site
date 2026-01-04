from django.db import models


class Pilot(models.Model):
    STATUS_CHOICES = [
        ('planning', 'Planning'),
        ('active', 'Active'),
        ('completed', 'Completed'),
    ]
    
    location = models.CharField(max_length=200)
    country = models.CharField(max_length=100, default='Kazakhstan')
    start_date = models.DateField(blank=True, null=True)
    duration_months = models.IntegerField(default=6, help_text="Expected duration in months")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    progress_percent = models.IntegerField(default=0, help_text="Progress percentage (0-100)")
    description = models.TextField(blank=True)
    nda_notice = models.TextField(
        blank=True,
        default="Pilot location details are subject to NDA. Contact us for more information."
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-start_date']
    
    def __str__(self):
        return f"Pilot - {self.location} ({self.status})"

