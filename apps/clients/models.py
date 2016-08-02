from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Client(models.Model):
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=200, default='', blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        ordering = ('created_at',)
        app_label = 'clients'
        db_table = 'app_client'
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'