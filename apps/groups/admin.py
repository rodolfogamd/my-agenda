from django.contrib import admin

from models import Group, GroupMember


class GroupAdmin(admin.ModelAdmin):
    model = Group
    list_display = ['id', 'name', 'active']
    search_fields = ['id', ]


class GroupMemberAdmin(admin.ModelAdmin):
    model = GroupMember
    list_display = ('id', 'user', 'group', 'alias')
    search_fields = ['id', 'user', 'group', 'alias']


admin.site.register(Group, GroupAdmin)
admin.site.register(GroupMember, GroupMemberAdmin)
