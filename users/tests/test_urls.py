from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.views import register
from middagsdeling import urls


class TestUrls(SimpleTestCase):

    def test_register_url_resolve(self):
        url = reverse('register')
        print(resolve(url))
        self.assertEquals(resolve(url).func, register)
