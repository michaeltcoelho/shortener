#encoding:utf-8
from django.test import TestCase, Client
from django.core.urlresolvers import reverse as r
from core.forms import UserCreationForm, AuthenticationForm

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

