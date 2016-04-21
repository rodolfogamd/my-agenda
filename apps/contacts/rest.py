import django_filters

from rest_framework import routers, viewsets, filters

from common.common import StandardResultsSetPagination
from serializers import ContactSerializer
from apps.contacts.models import Contact


class ContactsFilter(django_filters.FilterSet):
    class Meta:
        model = Contact
        fields = ('id', 'first_name', 'last_name', 'date_joined', 'location')


class ContactsViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ContactsFilter
