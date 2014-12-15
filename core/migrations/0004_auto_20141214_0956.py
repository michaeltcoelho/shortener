# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20141211_0705'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('visits', models.PositiveIntegerField(default=0, verbose_name='visitas')),
                ('link', models.ForeignKey(to='core.Link')),
                ('user', models.ForeignKey(to='core.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='link',
            options={},
        ),
        migrations.RemoveField(
            model_name='link',
            name='visits',
        ),
    ]
