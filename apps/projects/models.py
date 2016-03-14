from django.db import models

CLIENT_CHOICES = [('FIS', 'fis'), ('Iridium', 'iridium'), ('Lima3', 'lima3'), ('Clarabridge', 'Survey API')]


class Project(models.Model):
    name = models.CharField(max_length=200)
    client = models.CharField(choices=CLIENT_CHOICES, default='fis', max_length=100)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.name

    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        ordering = ('created_at',)
        app_label = 'projects'
        db_table = 'app_projects'
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
