from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Groups(models.Model):
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=200, blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('created_at',)
        app_label = 'groups'
        db_table = 'app_groups'
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'
