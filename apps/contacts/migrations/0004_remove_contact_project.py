# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20160312_1953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='project',
        ),
    ]
