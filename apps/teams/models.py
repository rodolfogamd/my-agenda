from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from apps.projects.models import Project
from apps.users.models import User
from apps.groups.models import Group


@python_2_unicode_compatible
class Team(models.Model):
    project = models.ForeignKey(Project, related_name='teams', related_query_name='team')
    owner = models.ForeignKey(User, related_name='teams', related_query_name='team')
    groups = models.ManyToManyField(Group, through='TeamGroup', related_name='teams', related_query_name='team')
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s - %s" % (self.project, self.owner)

    class Meta:
        ordering = ('created_at',)
        app_label = 'teams'
        db_table = 'app_team'
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'


@python_2_unicode_compatible
class TeamGroup(models.Model):
    team = models.ForeignKey(Team, related_name='team_groups', related_query_name='team_group')
    group = models.ForeignKey(Group, related_name='teams_groups', related_query_name='team_group')

    def __str__(self):
        return "%s - %s" % (self.team, self.group)

    class Meta:
        app_label = 'teams'
        db_table = 'app_team_group'
        verbose_name = 'Team Groups'
        verbose_name_plural = 'Teams Groups'
