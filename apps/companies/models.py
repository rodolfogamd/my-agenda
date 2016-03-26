from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=200, default='', blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        ordering = ('created_at',)
        app_label = 'companies'
        db_table = 'app_companies'
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'