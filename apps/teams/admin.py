from django.contrib import admin

from apps.teams.models import Team, TeamGroup


class TeamAdmin(admin.ModelAdmin):
    model = Team
    list_display = ['id', 'project', 'owner', 'active', 'created_at']
    search_fields = ['id', 'project', 'owner', 'active']


class TeamGroupAdmin(admin.ModelAdmin):
    model = TeamGroup
    list_display = ('id', 'team', 'group')
    search_fields = ['id', 'team', 'group']


admin.site.register(Team, TeamAdmin)
admin.site.register(TeamGroup, TeamGroupAdmin)
