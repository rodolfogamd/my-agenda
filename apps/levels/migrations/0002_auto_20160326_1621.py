# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levels', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='level',
            options={'ordering': ('name',), 'verbose_name': 'Level', 'verbose_name_plural': 'Levels'},
        ),
        migrations.RemoveField(
            model_name='level',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='level',
            name='modified_at',
        ),
    ]
