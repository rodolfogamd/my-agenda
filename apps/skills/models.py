from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=200, default='', blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.name

    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        ordering = ('name',)
        app_label = 'skills'
        db_table = 'app_skills'
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
