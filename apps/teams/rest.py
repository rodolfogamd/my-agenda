from django_filters import FilterSet
from rest_framework import routers, serializers, viewsets, filters

from common.common import StandardResultsSetPagination
from models import Team


class TeamSerializer(serializers.ModelSerializer):
    created = serializers.CharField(source='created_at')

    class Meta:
        model = Team
        fields = ('id', 'project', 'contact', 'active', 'created')

    def __unicode__(self):
        return "%s" % self.name


class TeamsFilter(FilterSet):
    class Meta:
        model = Team
        fields = ('id', 'project', 'contact', 'active')


# ViewSets define the view behavior.
class TeamsViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = TeamsFilter
