# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ('created_at',), 'verbose_name': 'Contact', 'verbose_name_plural': 'Contacts'},
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='active',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='skill',
        ),
        migrations.AddField(
            model_name='contact',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
        migrations.AddField(
            model_name='contact',
            name='first_name',
            field=models.CharField(max_length=250, verbose_name='first name', blank=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Enable user.', verbose_name='active'),
        ),
        migrations.AddField(
            model_name='contact',
            name='last_name',
            field=models.CharField(max_length=250, verbose_name='last name', blank=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 2, 23, 12, 49, 559202, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
