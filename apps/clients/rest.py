from django_filters import FilterSet
from rest_framework import routers, serializers, viewsets, filters

from common.common import StandardResultsSetPagination
from serializers import ClientSerializer
from models import Client


class ClientFilter(FilterSet):
    class Meta:
        model = Client
        fields = ('id', 'name', 'alias', 'active')


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ClientFilter
