from django.contrib import admin

from apps.teams.models import Team


class TeamAdmin(admin.ModelAdmin):
    model = Team
    list_display = ['id', 'project', 'contact', 'active', 'created_at']
    search_fields = ['id', 'project', 'contact', 'active']


admin.site.register(Team, TeamAdmin)