# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20141211_0703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='user',
            field=models.ManyToManyField(default=None, to=settings.AUTH_USER_MODEL, null=True, blank=True),
            preserve_default=True,
        ),
    ]
