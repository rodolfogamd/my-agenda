# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ('created_at',), 'verbose_name': 'Project', 'verbose_name_plural': 'Projects'},
        ),
        migrations.RenameField(
            model_name='project',
            old_name='created',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='project',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 1, 4, 14, 25, 790876, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
