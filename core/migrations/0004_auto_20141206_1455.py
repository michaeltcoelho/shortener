# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20141203_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='user',
            field=models.ForeignKey(related_name='user_link', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
