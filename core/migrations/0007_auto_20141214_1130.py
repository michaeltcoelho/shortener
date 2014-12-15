# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_link_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userlink',
            name='submitted',
        ),
        migrations.AddField(
            model_name='link',
            name='submitted',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 14, 13, 30, 54, 817181, tzinfo=utc), verbose_name='data', auto_now_add=True),
            preserve_default=False,
        ),
    ]
