# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0002_skill_alias'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ('created_at',), 'verbose_name': 'Skill', 'verbose_name_plural': 'Skills'},
        ),
        migrations.RenameField(
            model_name='skill',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='level',
        ),
        migrations.AddField(
            model_name='skill',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 1, 4, 12, 48, 925434, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='skill',
            name='alias',
            field=models.CharField(default=b'', max_length=200, blank=True),
        ),
    ]
