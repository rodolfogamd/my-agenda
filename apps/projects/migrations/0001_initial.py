# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('client', models.CharField(default=b'fis', max_length=100, choices=[(b'FIS', b'fis'), (b'Iridium', b'iridium'), (b'Lima3', b'lima3'), (b'Clarabridge', b'Survey API')])),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('created',),
                'db_table': 'app_projects',
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
    ]
