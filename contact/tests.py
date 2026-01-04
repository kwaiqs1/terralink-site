from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from .models import ContactRequest


class ContactFormTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('contact')
    
    def test_contact_form_displays(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Get in Touch')
    
    def test_contact_form_submission(self):
        data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'organization': 'Test Org',
            'message': 'Test message',
            'product_interest': 'general',
            'honeypot': '',  # Honeypot should be empty
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertTrue(ContactRequest.objects.filter(email='test@example.com').exists())
    
    def test_contact_form_honeypot(self):
        data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'Test message',
            'honeypot': 'spam',  # Honeypot filled = spam
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)  # Form error, not redirect
        self.assertFalse(ContactRequest.objects.filter(email='test@example.com').exists())

