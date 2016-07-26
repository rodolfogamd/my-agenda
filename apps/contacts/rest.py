import django_filters

from rest_framework import routers, viewsets, filters

from common.common import StandardResultsSetPagination
from serializers import ContactSerializer
from apps.contacts.models import Contact
from apps.teams.models import Team
from apps.levels.models import LevelSkill
from django.db.models.query import QuerySet


class ContactsFilter(django_filters.FilterSet):
    class Meta:
        model = Contact
        fields = ('id', 'first_name', 'last_name', 'date_joined', 'location')


class ContactsViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ContactsFilter

    def get_queryset(self):
        queryset = self.queryset

        if isinstance(queryset, QuerySet):
            queryset = queryset.all()

        project_name = self.request.query_params.get('project_name', None)
        skill_name = self.request.query_params.get('skill_name', None)

        if project_name is not None:
            team_list = Team.objects.filter(project__name__icontains=project_name).values('contact_id')
            queryset = queryset.filter(pk__in=team_list)

        if skill_name is not None:
            level_skill_list = LevelSkill.objects.filter(skill__name__icontains=skill_name).values('contact_id')
            queryset = queryset.filter(pk__in=level_skill_list)

        return queryset
