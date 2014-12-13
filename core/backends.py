#coding:utf-8
from django.contrib.auth import get_user_model
from .models import User

class AuthBackend(object):
    """
    AuthBackend - custom auth
    """
    def authenticate(self, email=None, password=None):
        """
        authenticate - auth an user by email and password
        """
        try:
            user = get_user_model().objects.get(email=email)
            if user.check_password(password):
                return user
        except User.DoesNotExist, e:
            return None
        return None

    def get_user(self, user_id):
        """
        get_user - return the user object by pk
        """
        try:
            return get_user_model().objects.get(pk=user_id)
        except User.DoesNotExist, e:
            return None