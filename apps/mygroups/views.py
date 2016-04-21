import django_filters
from rest_framework import routers, viewsets, filters

from common.common import StandardResultsSetPagination
from serializers import MyGroupsSerializer
from models import MyGroups


class MyGroupsFilter(django_filters.FilterSet):
    class Meta:
        model = MyGroups
        fields = ('id', 'group', 'user', 'active')


# ViewSets define the view behavior.
class MyGroupsViewSet(viewsets.ModelViewSet):
    queryset = MyGroups.objects.all()
    serializer_class = MyGroupsSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = MyGroupsFilter
