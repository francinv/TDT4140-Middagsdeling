from django.test import SimpleTestCase
from django.urls import reverse, resolve
from APP.views import home


class TestUrls(SimpleTestCase):

    def test_APP_home_url_resolve(self):
        url = reverse('APP-home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home)
