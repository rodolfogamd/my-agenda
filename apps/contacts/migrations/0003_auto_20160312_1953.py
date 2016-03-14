# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20160302_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='avatar_url',
            field=models.CharField(max_length=250, null=True, verbose_name='Avatar', blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='project',
            field=models.ForeignKey(related_name='project', blank=True, to='projects.Project', null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
