#encoding:utf-8
from django.contrib.auth import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

class UserManager(models.BaseUserManager):

  def _create_user(self, name, email, password, **extra_fields):

    now = timezone.now()

    if not email:
      raise ValueError(_('The given email must be set'))

    email = self.normalize_email(email)
    user  = self.model(name=name, email=email, joined=now, **extra_fields)

    if user:
      user.set_password(password)
      user.save(using=self._db)
    return user

  def create_user(self, name=None, email=None, password=None, **extra_fields):
    return self._create_user(name, email, password, **extra_fields)

  def create_superuser(self, name=None, email=None, password=None, **extra_fields):
    return self._create_user(name, email, password, **extra_fields)
