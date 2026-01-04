from django.shortcuts import render
from .models import Pilot


def pilot_status(request):
    """Pilot status page - safe with empty DB"""
    try:
        pilot = Pilot.objects.first()  # Get the active pilot
    except Exception:
        pilot = None
    
    return render(request, 'pilot/status.html', {
        'pilot': pilot,
    })

