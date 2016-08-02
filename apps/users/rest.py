import django_filters

from rest_framework import routers, viewsets, filters

from common.common import StandardResultsSetPagination
from serializers import UserSerializer
from apps.users.models import User
from django.db.models.query import QuerySet


class UsersFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'date_joined', 'location')


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = UsersFilter

    def get_queryset(self):
        queryset = self.queryset

        if isinstance(queryset, QuerySet):
            queryset = queryset.all()

        project_name = self.request.query_params.get('project_name', None)
        skill_name = self.request.query_params.get('skill_name', None)

        if project_name is not None:
            queryset = queryset.filter(group__team__project__name__icontains=project_name)

        if skill_name is not None:
            queryset = queryset.filter(skills__name__icontains=skill_name)

        return queryset
