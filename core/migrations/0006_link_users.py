# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20141214_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='users',
            field=models.ManyToManyField(to='core.User', through='core.UserLink'),
            preserve_default=True,
        ),
    ]
