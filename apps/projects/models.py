from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from apps.clients.models import Client


@python_2_unicode_compatible
class Project(models.Model):
    name = models.CharField(max_length=200)
    client = models.ForeignKey(Client, related_name='projects', related_query_name='project')
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('created_at',)
        app_label = 'projects'
        db_table = 'app_project'
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
