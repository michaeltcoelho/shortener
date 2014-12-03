# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(max_length=255, verbose_name='url')),
                ('submitted', models.DateTimeField(auto_now_add=True, verbose_name='data')),
                ('visits', models.PositiveIntegerField(default=0, verbose_name='visitas', db_index=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['visits'],
            },
            bases=(models.Model,),
        ),
    ]
