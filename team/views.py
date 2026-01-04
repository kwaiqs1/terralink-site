from django.shortcuts import render
from .models import TeamMember


def team_list(request):
    """Team page - safe with empty DB"""
    try:
        members = list(TeamMember.objects.all())
    except Exception:
        members = []
    
    return render(request, 'team/list.html', {
        'members': members,
    })

