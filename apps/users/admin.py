from django.contrib import admin

from apps.users.models import User
from apps.users.models import UserSkill


class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ['id', 'first_name', 'last_name', 'location']
    search_fields = ['id', 'location']


class UserSkillAdmin(admin.ModelAdmin):
    model = UserSkill
    list_display = ('id', 'level', 'skill', 'user', 'from_date',)
    search_fields = ['id', 'level', 'skill', 'user', 'from_date']


admin.site.register(User, UserAdmin)
admin.site.register(UserSkill, UserSkillAdmin)
