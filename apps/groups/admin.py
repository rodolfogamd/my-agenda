from django.contrib import admin

from models import Groups


class GroupsAdmin(admin.ModelAdmin):
    model = Groups
    list_display = ['id', 'name', 'active']
    search_fields = ['id', ]


admin.site.register(Groups, GroupsAdmin)
