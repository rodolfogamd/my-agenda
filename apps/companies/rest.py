from django_filters import FilterSet
from rest_framework import routers, serializers, viewsets, filters

from common.common import StandardResultsSetPagination
from models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'alias', 'active')

    def __unicode__(self):
        return self.name

    def create(self, validated_data):
        company = Company(
            name=validated_data['name'],
            alias=validated_data['name'].lower(),
            active=validated_data['active']
        )
        company.save()
        return company

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.alias = validated_data.get('name', instance.name).lower()
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance


class CompanyFilter(FilterSet):
    class Meta:
        model = Company
        fields = ('id', 'name', 'alias', 'active')


# ViewSets define the view behavior.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = CompanyFilter
