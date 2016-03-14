# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0003_auto_20160301_0412'),
        ('contacts', '0003_auto_20160312_1953'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('alias', models.CharField(default=b'', max_length=200, blank=True)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('created_at',),
                'db_table': 'app_levels',
                'verbose_name': 'Level',
                'verbose_name_plural': 'Levels',
            },
        ),
        migrations.CreateModel(
            name='LevelSkill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('from_date', models.DateField(null=True, blank=True)),
                ('contact', models.ForeignKey(related_name='_contact', to='contacts.Contact')),
                ('level', models.ForeignKey(related_name='_level', to='levels.Level')),
                ('skill', models.ForeignKey(related_name='_skill', to='skills.Skill')),
            ],
        ),
        migrations.AddField(
            model_name='level',
            name='skills',
            field=models.ManyToManyField(related_name='levels', through='levels.LevelSkill', to='skills.Skill'),
        ),
    ]
