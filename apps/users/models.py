from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from apps.skills.models import Skill
from apps.levels.models import Level


@python_2_unicode_compatible
class User(models.Model):
    first_name = models.CharField(_('first name'), max_length=250, blank=True)
    last_name = models.CharField(_('last name'), max_length=250, blank=True)
    avatar_url = models.CharField(_('Avatar'), max_length=250, blank=True, null=True)
    is_active = models.BooleanField(_('active'), default=True, help_text=_('Enable user.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    location = models.CharField(max_length=100, blank=True, default='')
    skills = models.ManyToManyField(Skill, through='UserSkill', related_name='users', related_query_name='user')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    class Meta:
        ordering = ('created_at',)
        app_label = 'users'
        db_table = 'app_user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


@python_2_unicode_compatible
class UserSkill(models.Model):
    level = models.ForeignKey(Level, related_name='user_skills', related_query_name='user_skill')
    skill = models.ForeignKey(Skill, related_name='user_skills', related_query_name='user_skill')
    user = models.ForeignKey(User, related_name='users_skills', related_query_name='user_skill')
    from_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return "%s has the level %s in skill %s from %s" % (self.user, self.level, self.skill, self.from_date)

    class Meta:
        app_label = 'users'
        db_table = 'app_user_skill'
        verbose_name = 'User Skills'
        verbose_name_plural = 'Users Skills'
