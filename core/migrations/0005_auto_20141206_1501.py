# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20141206_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='url',
            field=models.TextField(max_length=255, verbose_name='url', validators=[django.core.validators.URLValidator()]),
            preserve_default=True,
        ),
    ]
