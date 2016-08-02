from django.contrib import admin

from apps.clients.models import Client


class ClientAdmin(admin.ModelAdmin):
    model = Client
    list_display = ('id', 'name', 'active',)
    search_fields = ['id', 'name', 'active']

    def save_model(self, request, obj, form, change):
        obj.alias = obj.name.lower()
        obj.save()


admin.site.register(Client, ClientAdmin)
