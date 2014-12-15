#-*- coding: utf-8 -*-
from django.test import TestCase, Client
from django.core.urlresolvers import reverse as r
from core.models import User, Link
from core.forms import UserCreationForm, AuthenticationForm, LinkForm

class SignupFormTest(TestCase):
    """
    SignupFormTest -
    """
    def test_has_fields(self):
        """
        UserCreationForm must have 4 fields
        """
        form = UserCreationForm()

        self.assertItemsEqual(['name', 'email', 'password', 'confirm_password'], form.fields)

    def test_email_is_valid(self):
        """
        email must be a valid email address
        """
        form = self.form_validated(email='michael@gmail')
        self.assertItemsEqual(['email'], form.errors)

    def test_email_is_required(self):
        """
        email is required
        """
        form = self.form_validated(email='')
        self.assertItemsEqual(['email'], form.errors)

    def test_name_is_required(self):
        """
        name is required
        """
        form = self.form_validated(name='')
        self.assertItemsEqual(['name'], form.errors)

    def test_password_and_confirm_password_are_equals(self):
        """
        confirm password must be equals to password
        """
        form = self.form_validated(password='123', confirm_password='321')
        self.assertItemsEqual(['confirm_password'], form.errors)


    def form_validated(self, **kwargs):

        data = dict(name='Michael Coelho', email='michael.tcoelho@gmail.com',
                    password='123', confirm_password='123')

        data.update(kwargs)
        form = UserCreationForm(data)
        form.is_valid()
        return form

class AuthenticationFormTest(TestCase):
    """
    AuthenticationForm -
    """
    def test_has_fields(self):
        """
        AuthenticationForm must have 2 fields
        """
        form = AuthenticationForm()
        self.assertItemsEqual([ 'email', 'password' ], form.fields)

    def test_email_is_valid(self):
        """
        email must be a valid email address
        """
        form = self.form_validated(email='michael@gmail')
        self.assertItemsEqual(['email'], form.errors)

    def test_email_required(self):
        """
        email is required
        """
        form = self.form_validated(email='')
        self.assertItemsEqual(['email'], form.errors)

    def test_password_required(self):
        """
        password is required
        """
        form = self.form_validated(password='')
        self.assertItemsEqual(['password'], form.errors)

    def test_login_invalid(self):
        """
        login should be invalid
        """

        User.objects.create_user(name='Michael', email='michael.tcoelho@gmail.com', password='123')

        form = self.form_validated(email='michael.tcoelho@gmail.com', password='321')
        self.assertIn(form.error_messages['invalid_login'], form.non_field_errors())

    def test_login_valid(self):
        """
        login should be valid
        """
        User.objects.create_user(name='Michael', email='michael.tcoelho@gmail.com', password='123')

        data = dict(email='michael.tcoelho@gmail.com', password='123')

        form = AuthenticationForm(data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.non_field_errors(), [])

    def form_validated(self, **kwargs):
        """
        """
        data = dict(email='michael.tcoelho@gmail.com', password='123')

        data.update(kwargs)
        form = AuthenticationForm(data)
        form.is_valid()
        return form

class LinkFormTest(TestCase):
    """
    LinkFormTest
    """
    def test_has_fields(self):
        """
        LinkForm must have 1 field
        """
        form = LinkForm()

        self.assertItemsEqual(['url'], form.fields)

    def test_url_is_required(self):
        """
        url field is required
        """
        data = { 'url' : '' }

        form = LinkForm(data)
        self.assertItemsEqual(['url'], form.errors)

    def test_url_is_valid(self):
        """
        url must be a valid address
        """
        data = { 'url' : 'www.google.com' }

        form = LinkForm(data)
        self.assertTrue(form.is_valid())

    def test_url_is_invalid(self):
        """
        url must be a invalid address
        """
        data = { 'url' : 'www.google$%#.com' }

        form = LinkForm(data)
        self.assertFalse(form.is_valid())