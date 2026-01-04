from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Product, PricingPlan


def product_list(request):
    """Products listing page - safe with empty DB"""
    try:
        products = list(Product.objects.all())
    except Exception:
        products = []
    
    return render(request, 'products/list.html', {
        'products': products,
    })


def product_detail(request, slug):
    """Product detail page"""
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'products/detail.html', {
        'product': product,
    })


def pricing(request):
    """Pricing page - safe with empty DB"""
    try:
        ai_plans = list(PricingPlan.objects.filter(category='ai'))
        drone_plans = list(PricingPlan.objects.filter(category='drone'))
    except Exception:
        ai_plans = []
        drone_plans = []
    
    return render(request, 'products/pricing.html', {
        'ai_plans': ai_plans,
        'drone_plans': drone_plans,
    })

