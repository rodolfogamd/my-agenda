import django_filters
from rest_framework import routers, viewsets, filters

from common.common import StandardResultsSetPagination
from serializers import GroupsSerializer
from models import Groups


class GroupsFilter(django_filters.FilterSet):
    class Meta:
        model = Groups
        fields = ('id', 'name', 'active')


class GroupsViewSet(viewsets.ModelViewSet):
    queryset = Groups.objects.all()
    serializer_class = GroupsSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = GroupsFilter
