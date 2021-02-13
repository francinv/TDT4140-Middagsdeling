from django.test import TestCase, Client
from django.urls import reverse
from users.views import register
from middagsdeling import urls

import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')


    def test_register_request(self):
        response = self.client.get(self.register_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')



