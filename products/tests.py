from django.test import TestCase, Client
from django.urls import reverse
from .models import Product


class ProductModelTest(TestCase):
    def test_product_creation(self):
        product = Product.objects.create(
            title='Test Product',
            short_description='Test description',
            long_description='Long description',
            type='ai',
            status='pilot',
            features=['Feature 1', 'Feature 2']
        )
        self.assertEqual(product.slug, 'test-product')
        self.assertEqual(str(product), 'Test Product')


class ProductViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.product = Product.objects.create(
            title='Test Product',
            slug='test-product',
            short_description='Test description',
            long_description='Long description',
            type='ai',
            status='pilot',
            features=['Feature 1']
        )
    
    def test_product_list_view(self):
        response = self.client.get(reverse('products:product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Product')
    
    def test_product_detail_view(self):
        response = self.client.get(reverse('products:product_detail', args=['test-product']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Product')

