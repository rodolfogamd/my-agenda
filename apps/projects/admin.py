from django.contrib import admin

from apps.projects.models import Project


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ['id', 'name', 'client', 'active', 'created_at']
    search_fields = ['id', 'name', 'client', 'active']


admin.site.register(Project, ProjectAdmin)
