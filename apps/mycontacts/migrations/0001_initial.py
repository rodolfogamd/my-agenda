# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contacts', '0004_remove_contact_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('contact', models.ForeignKey(to='contacts.Contact')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created_at',),
                'db_table': 'app_my_contact',
                'verbose_name': 'MyContact',
                'verbose_name_plural': 'MyContacts',
            },
        ),
    ]
