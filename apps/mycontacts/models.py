from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

from apps.contacts.models import Contact


@python_2_unicode_compatible
class MyContact(models.Model):
    contact = models.ForeignKey(Contact)
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('created_at',)
        app_label = 'mycontacts'
        db_table = 'app_my_contact'
        verbose_name = 'MyContact'
        verbose_name_plural = 'MyContacts'
