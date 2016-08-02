from django.contrib import admin
from apps.levels.models import Level


class LevelAdmin(admin.ModelAdmin):
    model = Level
    list_display = ('id', 'name', 'active',)
    search_fields = ['id', 'name', 'active']

    def save_model(self, request, obj, form, change):
        obj.alias = obj.name.lower()
        obj.save()

admin.site.register(Level, LevelAdmin)
