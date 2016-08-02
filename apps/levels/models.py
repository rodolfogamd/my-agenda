from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Level(models.Model):
    name = models.CharField(max_length=250)
    alias = models.CharField(max_length=250, default='', blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        app_label = 'levels'
        db_table = 'app_levels'
        verbose_name = 'Level'
        verbose_name_plural = 'Levels'
