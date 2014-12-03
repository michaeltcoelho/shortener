#encoding:utf-8
from django.test import TestCase
from django.db import IntegrityError
from core.models import User, Link

class UserModelTest(TestCase):

    def setUp(self):
        self.user = User(
            name='Michael',
            email='michael.tcoelho@gmail.com',
            password='123'
        )

    def test_user_creation(self):
        """
        user creation
        """
        self.user.save()

        self.assertEqual(1, self.user.pk)

    def test_user_unicode(self):
        """
        unicode
        """
        self.user.save()

        self.assertEqual(self.user.__unicode__(), 'Michael - michael.tcoelho@gmail.com')


class UserModelIntegrityTest(TestCase):

    def setUp(self):
        User.objects.create_user(name='Michael',
                                 email='michael.tcoelho@gmail.com',
                                 password='123')

    def test_unique_email(self):
        """
        email must be unique
        """
        u = User(name='Joao',
                 email='michael.tcoelho@gmail.com',
                 password='123')

        self.assertRaises(IntegrityError, u.save)

    def test_unique_name(self):
        """
        name must be unique
        """
        u = User(name='Michael',
                 email='joao@gmail.com',
                 password='123')

        self.assertRaises(IntegrityError, u.save)

class LinkModelTest(TestCase):
    """
    LinkModelTest
    """
    def setUp(self):
        self.user = User.objects.create_user(name='michael', email='michael.tcoelho@gmail.com', password='123')
        self.link = Link(url='www.google.com')

    def test_link_creation(self):
        """
        link creation to an user
        """
        self.user.save()

        self.link.user = self.user
        self.link.save()

        u = '%s - %s' % (self.link.url, self.link.to_base64())

        self.assertEqual(1, self.link.pk)
        self.assertEqual(self.link.__unicode__(), u)

    def test_link_creation_user_anonymous(self):
        """
        link creation to an anonymous user
        """
        self.link.save()
        self.assertEqual(1, self.link.pk)
