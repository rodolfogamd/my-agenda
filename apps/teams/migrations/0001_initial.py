# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_remove_contact_project'),
        ('projects', '0003_auto_20160326_1816'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('contact', models.ForeignKey(related_query_name=b'contact', related_name='contacts', to='contacts.Contact')),
                ('project', models.ForeignKey(related_query_name=b'project', related_name='projects', to='projects.Project')),
            ],
            options={
                'ordering': ('created_at',),
                'db_table': 'app_teams',
                'verbose_name': 'Team',
                'verbose_name_plural': 'Teams',
            },
        ),
    ]
