from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

class User(AbstractBaseUser):
    name  = models.CharField(_('Name'), max_length=150, required=True)
    email = models.EmailField(_('Email'), max_length=255, required=True)

    USERNAME_FIELDS = 'email'

    def __unicode__(self):
        return '<%s:%s>' % (self.name, self.email, )

    def get_full_name(self):
        return '%s' % self.name

    def get_short_name(self):
        return '%s' % self.name







