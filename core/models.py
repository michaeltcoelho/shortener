from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse as r
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.core.validators import URLValidator
from core.converter import base62

from managers import UserManager

class User(AbstractBaseUser):
    """
    User is the app`s user model
    """
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

class Link(models.Model):
    """
    Link is the user link to shorten it
    """
    user      = models.ManyToManyField(User)
    url       = models.URLField(_('url'), max_length=255)
    submitted = models.DateTimeField(_('data'), auto_now_add=True)
    visits    = models.PositiveIntegerField(_('visitas'), default=0, db_index=True)

    class Meta:
        ordering = ['-visits']

    def __unicode__(self):
        return '%s - %s' % (self.url, self.to_base62(), )

    def to_base62(self):
        return base62.from_decimal(self.id)

    def get_absolute_url(self):
        return r('core:redirect', args=[self.to_base62(), ])

    def get_shortened_url(self):
        return '{0}{1}'.format(settings.BASE_URL, self.to_base62())

    def to_json(self):
        return {
            'user' : self.user.email if self.user else None,
            'url'  : self.url,
            'submitted' : self.submitted.strftime('%d/%m/%Y %H:%m'),
            'visits' : self.visits,
            'shortened_url' : self.get_shortened_url()
        }