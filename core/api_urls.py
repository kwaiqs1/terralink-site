from django.urls import path
from . import api_views

urlpatterns = [
    path('products/', api_views.products_list, name='api_products_list'),
    path('products/<slug:slug>/', api_views.product_detail_api, name='api_product_detail'),
    path('contact/', api_views.contact_api, name='api_contact'),
    path('pilot-status/', api_views.pilot_status_api, name='api_pilot_status'),
]
