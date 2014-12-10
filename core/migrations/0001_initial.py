# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('name', models.CharField(unique=True, max_length=150, verbose_name='Name', db_index=True)),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name='Email', db_index=True)),
                ('joined', models.DateTimeField(auto_now_add=True, verbose_name='Joined')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(max_length=255, verbose_name='url')),
                ('submitted', models.DateTimeField(auto_now_add=True, verbose_name='data')),
                ('visits', models.PositiveIntegerField(default=0, verbose_name='visitas', db_index=True)),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-visits'],
            },
            bases=(models.Model,),
        ),
    ]
