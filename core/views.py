from django.shortcuts import render
from django.db import models


def home(request):
    """Home page / Hero block - safe with empty DB"""
    try:
        from products.models import Product
        products = list(Product.objects.all()[:2])
    except (models.OperationalError, ImportError):
        # Table doesn't exist yet or model not available
        products = []
    
    return render(request, 'core/home.html', {
        'products': products,
    })


def how_it_works(request):
    """How It Works page"""
    return render(request, 'core/how_it_works.html')


def technology(request):
    """Technology / Core Features page"""
    return render(request, 'core/technology.html')


def privacy(request):
    """Privacy policy page"""
    return render(request, 'core/privacy.html')


def terms(request):
    """Terms of service page"""
    return render(request, 'core/terms.html')

