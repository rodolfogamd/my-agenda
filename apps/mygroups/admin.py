from django.contrib import admin

from models import MyGroups


class MyGroupsAdmin(admin.ModelAdmin):
    model = MyGroups
    list_display = ['id', 'user', 'group', 'active']
    search_fields = ['id', 'user']


admin.site.register(MyGroups, MyGroupsAdmin)
