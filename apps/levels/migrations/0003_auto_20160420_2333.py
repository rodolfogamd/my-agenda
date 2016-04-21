# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levels', '0002_auto_20160326_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='alias',
            field=models.CharField(default='', max_length=250, blank=True),
        ),
        migrations.AlterField(
            model_name='level',
            name='name',
            field=models.CharField(max_length=250),
        ),
    ]
