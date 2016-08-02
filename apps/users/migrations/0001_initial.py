# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('levels', '0001_initial'),
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=250, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=250, verbose_name='last name', blank=True)),
                ('avatar_url', models.CharField(max_length=250, null=True, verbose_name='Avatar', blank=True)),
                ('is_active', models.BooleanField(default=True, help_text='Enable user.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('location', models.CharField(default='', max_length=100, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('created_at',),
                'db_table': 'app_user',
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='UserSkill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('from_date', models.DateField(null=True, blank=True)),
                ('level', models.ForeignKey(related_query_name='user_skill', related_name='user_skills', to='levels.Level')),
                ('skill', models.ForeignKey(related_query_name='user_skill', related_name='user_skills', to='skills.Skill')),
                ('user', models.ForeignKey(related_query_name='user_skill', related_name='users_skills', to='users.User')),
            ],
            options={
                'db_table': 'app_user_skill',
                'verbose_name': 'User Skills',
                'verbose_name_plural': 'Users Skills',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='skills',
            field=models.ManyToManyField(related_query_name='user', related_name='users', through='users.UserSkill', to='skills.Skill'),
        ),
    ]
