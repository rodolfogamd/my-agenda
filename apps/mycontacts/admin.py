from django.contrib import admin

from apps.mycontacts.models import MyContact


class MyContactAdmin(admin.ModelAdmin):
    model = MyContact
    list_display = ['id', 'user', 'contact', 'is_active']
    search_fields = ['id', ]


admin.site.register(MyContact, MyContactAdmin)
