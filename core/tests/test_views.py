#encoding:utf-8
from django.test import TestCase, Client
from django.core.urlresolvers import reverse as r
from core.forms import UserCreationForm, AuthenticationForm
from core.models import Link
from django.conf import settings

import json

client = Client()

class HomeTest(TestCase):
    """
    HomeTest -
    """
    def setUp(self):
        self.resp = client.get(r('core:home'))

    def test_get(self):
        """
        GET / should return status 200
        """
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """
        Template index.html
        """
        self.assertTemplateUsed(self.resp, 'index.html')

class SignupTest(TestCase):

    def setUp(self):
        self.resp = client.get(r('core:signup'))

    def test_get(self):
        """
        GET /signup should return status 200
        """
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """
        Template signup.html
        """
        self.assertTemplateUsed(self.resp, 'register/signup.html')

    def test_has_form(self):
        """
        must have the register/signup form
        """
        form = self.resp.context['form']
        self.assertIsInstance(form, UserCreationForm)

class LoginTest(TestCase):

    def setUp(self):
        self.resp = client.get(r('core:login'))

    def test_get(self):
        """
        GET /login should return status 200
        """
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """
        Template register/login.html
        """
        self.assertTemplateUsed(self.resp, 'register/login.html')

    def test_has_form(self):
        """
        must have the login form
        """
        form = self.resp.context['form']
        self.assertIsInstance(form, AuthenticationForm)

class ShortenTest(TestCase):
    """
    ShortenTest -
    """
    def setUp(self):
        self.link = Link(url="http://www.globoesporte.globo.com/")

    def test_get(self):
        """
        AJAX POST /short should return 200
        """
        data = { 'url' : 'www.google.com' }
        kwargs = { 'HTTP_X_REQUESTED_WITH' : 'XMLHttpRequest' }

        resp  = client.get(r('core:shorten'), data, **kwargs)

        self.assertEqual(200, resp.status_code)

    def test_url_shortened_valid_url(self):
        """
        Valid URL, must
        """
        data   = { 'url': 'www.google.com' }
        kwargs = { 'HTTP_X_REQUESTED_WITH':'XMLHttpRequest' }

        resp   = client.get(r('core:shorten'), data=data, **kwargs)

        o = json.loads(resp.content, encoding='utf8')

        self.assertNotIn('error', o)

    def test_url_shortened_invalid_url(self):
        """
        Invalid URL
        """
        data   = { 'url': 'www.#$$%$#$.com' }
        kwargs = { 'HTTP_X_REQUESTED_WITH':'XMLHttpRequest' }

        resp   = client.get(r('core:shorten'), data=data, **kwargs)

        o = json.loads(resp.content, encoding='utf8')

        self.assertIn('error', o)

    def test_url_shortened_url_required(self):
        """
        URL is required
        """
        data   = { 'url': '' }
        kwargs = { 'HTTP_X_REQUESTED_WITH':'XMLHttpRequest' }

        resp   = client.get(r('core:shorten'), data=data, **kwargs)

        o = json.loads(resp.content, encoding='utf8')

        self.assertIn('error', o)

    def test_url_shortened_must_be_unique(self):
        """
        The url shortened must be an unique url, if the user to shorten the same url,
        and it exists on database, must return it
        """
        self.link.save()

        url = {}
        url['shortened_url'] = '{0}{1}'.format(settings.BASE_URL, 1)

        data   = { 'url': 'www.globoesporte.globo.com' }
        kwargs = { 'HTTP_X_REQUESTED_WITH':'XMLHttpRequest' }

        resp   = self.client.get(r('core:shorten'), data=data, **kwargs)

        o = json.loads(resp.content, encoding='utf8')

        self.assertDictContainsSubset(url, o)

class RedirectTest(TestCase):
    """
    RedirectTest -
    """
    def setUp(self):
        Link.objects.create(url='http://www.google.com')

    def test_redirect_success(self):
        """
        Should return status code 301
        """
        resp = client.get(r('core:redirect', args=[1, ]))

        self.assertEqual(301, resp.status_code)

    def test_redirect_404(self):
        """
        Should return status code 404
        """
        resp = client.get(r('core:redirect', args=[0, ]))

        self.assertEqual(404, resp.status_code)