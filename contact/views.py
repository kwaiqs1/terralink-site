from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.http import JsonResponse
from .models import ContactRequest
from .forms import ContactForm


@require_http_methods(["GET", "POST"])
def contact(request):
    """Contact form page"""
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            # Rate limiting check (safe if table doesn't exist)
            ip_address = get_client_ip(request)
            try:
                recent_requests = ContactRequest.objects.filter(
                    ip_address=ip_address,
                    created_at__gte=timezone.now() - timezone.timedelta(hours=1)
                ).count()
                
                if recent_requests >= 5:
                    messages.error(request, 'Too many requests. Please try again later.')
                    return render(request, 'contact/form.html', {'form': form})
            except Exception:
                # If table doesn't exist, skip rate limiting
                pass
            
            # Save contact request
            contact_request = form.save(commit=False)
            contact_request.ip_address = ip_address
            contact_request.save()
            
            # Send email
            try:
                send_mail(
                    subject=f'New Contact Request from {contact_request.name}',
                    message=f'''
Name: {contact_request.name}
Email: {contact_request.email}
Organization: {contact_request.organization or "N/A"}
Product Interest: {contact_request.get_product_interest_display()}
Message:
{contact_request.message}
                    ''',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=False,
                )
            except Exception as e:
                # Log error but don't fail the request
                print(f"Email sending failed: {e}")
            
            messages.success(request, 'Thank you! We will get back to you soon.')
            return redirect('contact')
    else:
        product_interest = request.GET.get('product', '')
        initial = {'product_interest': product_interest} if product_interest else {}
        form = ContactForm(initial=initial)
    
    return render(request, 'contact/form.html', {'form': form})


def get_client_ip(request):
    """Get client IP address from request"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

