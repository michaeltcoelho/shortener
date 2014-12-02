#encoding:utf-8
from django.test import TestCase, Client
from django.core.urlresolvers import reverse as r

client = Client()

class HomeTest(TestCase):

    def setUp(self):
        self.resp = client.get(r('core:home'))

    def test_get(self):
        """
        GET / should return status 200
        """
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """
        Template
        """
        self.assertTemplateUsed(self.resp, 'index.html')
