# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('admin', models.OneToOneField(related_query_name='managed_group', related_name='managed_groups', null=True, blank=True, to='users.User')),
            ],
            options={
                'ordering': ('created_at',),
                'db_table': 'app_group',
                'verbose_name': 'Group',
                'verbose_name_plural': 'Group',
            },
        ),
        migrations.CreateModel(
            name='GroupMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alias', models.CharField(default='', max_length=200, blank=True)),
                ('group', models.ForeignKey(related_query_name='group_member', related_name='group_members', to='groups.Group')),
                ('user', models.ForeignKey(related_query_name='group_member', related_name='group_members', to='users.User')),
            ],
            options={
                'db_table': 'app_group_member',
                'verbose_name': 'Group Members',
                'verbose_name_plural': 'Groups Members',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='users',
            field=models.ManyToManyField(related_query_name='group', related_name='groups', through='groups.GroupMember', to='users.User'),
        ),
    ]
