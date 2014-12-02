from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from managers import UserManager

class User(AbstractBaseUser):
    name   = models.CharField(_('Name'), max_length=150, db_index=True, unique=True)
    email  = models.EmailField(_('Email'), max_length=255, db_index=True, unique=True)
    joined = models.DateTimeField(_('Joined'), auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'name', ]

    objects = UserManager()

    def __unicode__(self):
        return '%s - %s' % (self.name, self.email, )

    def get_full_name(self):
        return '%s' % self.name

    def get_short_name(self):
        return '%s' % self.name