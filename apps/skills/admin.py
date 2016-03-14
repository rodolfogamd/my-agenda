from django.contrib import admin
from apps.skills.models import Skill


class SkillAdmin(admin.ModelAdmin):
    model = Skill
    list_display = ['id', 'name', 'active']
    search_fields = ['id', 'name', 'active']

    def save_model(self, request, obj, form, change):
        obj.alias = obj.name.lower()
        obj.save()


admin.site.register(Skill, SkillAdmin)
