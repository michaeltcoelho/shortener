#coding:utf-8
from django.contrib.auth import get_user_model
from .models import User

class AuthBackend(object):
    """
    AuthBackend
    """
    def authenticate(self, email=None, password=None):
        try:
            user = get_user_model().objects.get(email=email)
            if user.check_password(password):
                return user
        except User.DoesNotExist, e:
            return None
        return None

    def get_user(self, user_id):
        try:
            return get_user_model().objects.get(pk=user_id)
        except User.DoesNotExist, e:
            return None