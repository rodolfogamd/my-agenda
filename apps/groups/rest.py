import django_filters
from rest_framework import routers, viewsets, filters

from common.common import StandardResultsSetPagination
from serializers import GroupsSerializer
from models import Group


class GroupsFilter(django_filters.FilterSet):
    class Meta:
        model = Group
        fields = ('id', 'name', 'admin', 'active')


class GroupsViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupsSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = GroupsFilter
