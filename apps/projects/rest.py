import django_filters
from rest_framework import routers, serializers, viewsets, filters

from common.common import StandardResultsSetPagination
from models import Project


class ProjectSerializer(serializers.ModelSerializer):
    created = serializers.CharField(source='created_at')

    class Meta:
        model = Project
        fields = ('id', 'name', 'client', 'active', 'created')

    def __unicode__(self):
        return "%s" % self.name


class ProjectsFilter(django_filters.FilterSet):
    class Meta:
        model = Project
        fields = ('id', 'name', 'client', 'active')


# ViewSets define the view behavior.
class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ProjectsFilter
