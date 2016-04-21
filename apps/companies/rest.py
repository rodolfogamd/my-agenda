from django_filters import FilterSet
from rest_framework import routers, serializers, viewsets, filters

from common.common import StandardResultsSetPagination
from serializers import CompanySerializer
from models import Company


class CompanyFilter(FilterSet):
    class Meta:
        model = Company
        fields = ('id', 'name', 'alias', 'active')


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = CompanyFilter
