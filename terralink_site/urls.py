"""
URL configuration for terralink_site project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from core.sitemaps import StaticViewSitemap, ProductSitemap
from products.views import pricing
from django.urls import re_path
from django.views.static import serve


sitemaps = {
    'static': StaticViewSitemap,
    'products': ProductSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('products/', include('products.urls')),
    path('pricing/', pricing, name='pricing'),
    path('team/', include('team.urls')),
    path('contact/', include('contact.urls')),
    path('pilot/', include('pilot.urls')),
    path('api/', include('core.api_urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain'), name='robots'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += [
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
]

