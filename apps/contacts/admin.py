from django.contrib import admin
from apps.contacts.models import Contact


class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = ['id', 'first_name', 'last_name', 'location', 'project']
    search_fields = ['id', 'location', 'project']


admin.site.register(Contact, ContactAdmin)
