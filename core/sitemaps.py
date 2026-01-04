from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from products.models import Product


class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'monthly'
    
    def items(self):
        return [
            'home',
            'how_it_works',
            'technology',
            'products:product_list',
            'pricing',
            'team_list',
            'pilot_status',
            'contact',
        ]
    
    def location(self, item):
        return reverse(item)


class ProductSitemap(Sitemap):
    priority = 0.9
    changefreq = 'weekly'
    
    def items(self):
        return Product.objects.all()
    
    def location(self, obj):
        return reverse('products:product_detail', args=[obj.slug])
    
    def lastmod(self, obj):
        return obj.updated_at

