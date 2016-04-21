import django_filters

from rest_framework import routers, viewsets, filters

from common.common import StandardResultsSetPagination
from serializers import MyContactSerializer
from apps.mycontacts.models import MyContact


class MyContactsFilter(django_filters.FilterSet):
    class Meta:
        model = MyContact
        fields = ('id', 'user', 'contact')


class MyContactsViewSet(viewsets.ModelViewSet):
    queryset = MyContact.objects.all()
    serializer_class = MyContactSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = MyContactsFilter
