# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('alias', models.CharField(default='', max_length=250, blank=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('name',),
                'db_table': 'app_levels',
                'verbose_name': 'Level',
                'verbose_name_plural': 'Levels',
            },
        ),
    ]
