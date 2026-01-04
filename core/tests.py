from django.test import TestCase, Client
from django.urls import reverse


class HomeViewTest(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_home_page_loads(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'TerraLink')
    
    def test_how_it_works_page_loads(self):
        response = self.client.get(reverse('how_it_works'))
        self.assertEqual(response.status_code, 200)
    
    def test_technology_page_loads(self):
        response = self.client.get(reverse('technology'))
        self.assertEqual(response.status_code, 200)

