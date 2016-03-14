from django.contrib import admin
from apps.levels.models import Level, LevelSkill


class LevelAdmin(admin.ModelAdmin):
    model = Level
    list_display = ('id', 'name', 'active',)
    search_fields = ['id', 'name', 'active']

    def save_model(self, request, obj, form, change):
        obj.alias = obj.name.lower()
        obj.save()


class LevelSkillAdmin(admin.ModelAdmin):
    model = LevelSkill
    list_display = ('id', 'level', 'skill', 'contact', 'from_date',)
    search_fields = ['id', 'level', 'skill', 'from_date']


admin.site.register(Level, LevelAdmin)
admin.site.register(LevelSkill, LevelSkillAdmin)
