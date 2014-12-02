#encoding:utf-8
from django.test import TestCase
from django.db import IntegrityError
from core.models import User

class UserTest(TestCase):

    def setUp(self):
        self.user = User(
            name='Michael',
            email='michael.tcoelho@gmail.com',
            password='123'
        )

    def test_user_creation(self):

        self.user.save()

        self.assertEqual(1, self.user.pk)

    def test_user_unicode(self):

        self.user.save()

        self.assertEqual(self.user.__unicode__(), 'Michael - michael.tcoelho@gmail.com')


class UserIntegrityTest(TestCase):

    def setUp(self):
        User.objects.create_user(name='Michael',
                                 email='michael.tcoelho@gmail.com',
                                 password='123')

    def test_unique_email(self):

        u = User(name='Joao',
                 email='michael.tcoelho@gmail.com',
                 password='123')

        self.assertRaises(IntegrityError, u.save)

    def test_unique_name(self):

        u = User(name='Michael',
                 email='joao@gmail.com',
                 password='123')

        self.assertRaises(IntegrityError, u.save)
