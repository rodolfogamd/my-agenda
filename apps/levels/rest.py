import django_filters
from rest_framework import routers, serializers, viewsets, filters

from common.common import StandardResultsSetPagination
from models import Level


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('id', 'name', 'alias', 'active')

    def __unicode__(self):
        return self.name

    def create(self, validated_data):
        level = Level(
            name=validated_data['name'],
            alias=validated_data['name'].lower(),
            active=validated_data['active']
        )
        level.save()
        return level

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.alias = validated_data.get('name', instance.name).lower()
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance


class LevelFilter(django_filters.FilterSet):
    class Meta:
        model = Level
        fields = ('id', 'name', 'alias', 'active')


# ViewSets define the view behavior.
class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = LevelFilter
