from django.test import TestCase, Client
from django.urls import reverse
from APP.views import home
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('APP-home')

    def test_home_request(self):
        response = self.client.get(self.home_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'APP/index.html')

