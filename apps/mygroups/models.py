from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

from apps.groups.models import Groups


@python_2_unicode_compatible
class MyGroups(models.Model):
    user = models.ForeignKey(User)
    group = models.ForeignKey(Groups)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        ordering = ('created_at',)
        app_label = 'mygroups'
        db_table = 'app_my_groups'
        verbose_name = 'MyGroup'
        verbose_name_plural = 'MyGroups'
