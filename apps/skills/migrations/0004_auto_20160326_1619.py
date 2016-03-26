# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0003_auto_20160301_0412'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ('name',), 'verbose_name': 'Skill', 'verbose_name_plural': 'Skills'},
        ),
        migrations.RemoveField(
            model_name='skill',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='modified_at',
        ),
    ]
