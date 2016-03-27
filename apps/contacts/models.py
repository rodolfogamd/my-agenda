from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.utils import timezone


class Contact(models.Model):
    first_name = models.CharField(_('first name'), max_length=250, blank=True)
    last_name = models.CharField(_('last name'), max_length=250, blank=True)
    avatar_url = models.CharField(_('Avatar'), max_length=250, blank=True, null=True)
    is_active = models.BooleanField(_('active'), default=True, help_text=_('Enable user.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    user = models.ForeignKey(User, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)

    class Meta:
        ordering = ('created_at',)
        app_label = 'contacts'
        db_table = 'app_contacts'
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
