#coding:utf-8
from django.contrib.auth import get_user_model

class AuthBackend(object):
    """
    AuthBackend
    """
    def authenticate(self, email=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email__exact=email)
            if user.check_password(password):
                return user
        except Exception, e:
            return None

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except Exception, e:
            return None