from django.db import models

from apps.projects.models import Project
from apps.contacts.models import Contact


class Team(models.Model):
    project = models.ForeignKey(Project, related_name='projects', related_query_name='project')
    contact = models.ForeignKey(Contact, related_name='contacts', related_query_name='contact')
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s - %s" % (self.project, self.contact)

    class Meta:
        ordering = ('created_at',)
        app_label = 'teams'
        db_table = 'app_teams'
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'