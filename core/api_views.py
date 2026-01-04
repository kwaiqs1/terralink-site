from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product
from contact.forms import ContactForm
from contact.models import ContactRequest
from pilot.models import Pilot
from django.utils import timezone
from django.shortcuts import get_object_or_404


@api_view(['GET'])
def products_list(request):
    """API endpoint for products list - safe with empty DB"""
    try:
        products = Product.objects.all()
        data = [{
            'id': p.id,
            'title': p.title,
            'slug': p.slug,
            'short_description': p.short_description,
            'type': p.type,
            'status': p.status,
            'features': p.features,
        } for p in products]
    except Exception:
        data = []
    return Response(data)


@api_view(['GET'])
def product_detail_api(request, slug):
    """API endpoint for product detail"""
    try:
        product = Product.objects.get(slug=slug)
        data = {
            'id': product.id,
            'title': product.title,
            'slug': product.slug,
            'short_description': product.short_description,
            'long_description': product.long_description,
            'type': product.type,
            'status': product.status,
            'features': product.features,
            'icon_svg': product.icon_svg,
        }
        return Response(data)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=404)


@api_view(['POST'])
def contact_api(request):
    """API endpoint for contact form submission - safe with empty DB"""
    form = ContactForm(request.data, request.FILES)
    if form.is_valid():
        # Rate limiting (safe if table doesn't exist)
        ip_address = request.META.get('REMOTE_ADDR', '')
        try:
            recent_requests = ContactRequest.objects.filter(
                ip_address=ip_address,
                created_at__gte=timezone.now() - timezone.timedelta(hours=1)
            ).count()
            
            if recent_requests >= 5:
                return Response({'error': 'Too many requests'}, status=429)
        except Exception:
            # If table doesn't exist, skip rate limiting
            pass
        
        try:
            contact_request = form.save(commit=False)
            contact_request.ip_address = ip_address
            contact_request.save()
            return Response({'status': 'success', 'message': 'Thank you for your message!'})
        except Exception as e:
            return Response({'status': 'error', 'message': 'Database error. Please try again later.'}, status=500)
    else:
        return Response({'status': 'error', 'errors': form.errors}, status=400)


@api_view(['GET'])
def pilot_status_api(request):
    """API endpoint for pilot status - safe with empty DB"""
    try:
        pilot = Pilot.objects.first()
        if pilot:
            data = {
                'location': pilot.location,
                'country': pilot.country,
                'status': pilot.status,
                'progress_percent': pilot.progress_percent,
                'duration_months': pilot.duration_months,
            }
            return Response(data)
    except Exception:
        pass
    return Response({'error': 'No pilot data'}, status=404)

