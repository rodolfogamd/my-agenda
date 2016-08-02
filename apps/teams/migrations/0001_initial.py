# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
        ('users', '0001_initial'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('created_at',),
                'db_table': 'app_team',
                'verbose_name': 'Team',
                'verbose_name_plural': 'Teams',
            },
        ),
        migrations.CreateModel(
            name='TeamGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group', models.ForeignKey(related_query_name='team_group', related_name='teams_groups', to='groups.Group')),
                ('team', models.ForeignKey(related_query_name='team_group', related_name='team_groups', to='teams.Team')),
            ],
            options={
                'db_table': 'app_team_group',
                'verbose_name': 'Team Groups',
                'verbose_name_plural': 'Teams Groups',
            },
        ),
        migrations.AddField(
            model_name='team',
            name='groups',
            field=models.ManyToManyField(related_query_name='team', related_name='teams', through='teams.TeamGroup', to='groups.Group'),
        ),
        migrations.AddField(
            model_name='team',
            name='owner',
            field=models.ForeignKey(related_query_name='team', related_name='teams', to='users.User'),
        ),
        migrations.AddField(
            model_name='team',
            name='project',
            field=models.ForeignKey(related_query_name='team', related_name='teams', to='projects.Project'),
        ),
    ]
