# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20141214_0956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='submitted',
        ),
        migrations.RemoveField(
            model_name='link',
            name='user',
        ),
        migrations.AddField(
            model_name='userlink',
            name='submitted',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 14, 12, 0, 16, 147196, tzinfo=utc), verbose_name='data', auto_now_add=True),
            preserve_default=False,
        ),
    ]
