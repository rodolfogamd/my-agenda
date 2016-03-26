from django.contrib import admin

from apps.companies.models import Company


class CompanyAdmin(admin.ModelAdmin):
    model = Company
    list_display = ('id', 'name', 'active',)
    search_fields = ['id', 'name', 'active']

    def save_model(self, request, obj, form, change):
        obj.alias = obj.name.lower()
        obj.save()


admin.site.register(Company, CompanyAdmin)
