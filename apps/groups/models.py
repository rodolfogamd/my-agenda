from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from apps.users.models import User


@python_2_unicode_compatible
class Group(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    users = models.ManyToManyField(User, through='GroupMember', related_name='groups', related_query_name='group')
    admin = models.OneToOneField(User, related_name='managed_groups', related_query_name='managed_group', blank=True,
                                 null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('created_at',)
        app_label = 'groups'
        db_table = 'app_group'
        verbose_name = 'Group'
        verbose_name_plural = 'Group'


@python_2_unicode_compatible
class GroupMember(models.Model):
    user = models.ForeignKey(User, related_name='group_members', related_query_name='group_member')
    group = models.ForeignKey(Group, related_name='group_members', related_query_name='group_member')
    alias = models.CharField(max_length=200, default='', blank=True)

    def __str__(self):
        return "%s - %s" % (self.group, self.user)

    class Meta:
        app_label = 'groups'
        db_table = 'app_group_member'
        verbose_name = 'Group Members'
        verbose_name_plural = 'Groups Members'