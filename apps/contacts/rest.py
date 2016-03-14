import django_filters

from rest_framework import routers, serializers, viewsets, filters

from common.common import StandardResultsSetPagination
from apps.contacts.models import Contact
from apps.projects.models import Project
from apps.levels.models import LevelSkill


class ContactSerializer(serializers.ModelSerializer):
    project = serializers.SlugRelatedField(slug_field='name', queryset=Project.objects.all())
    # level_skills = LevelSkill.objects.filter(contact=)
    name = serializers.CharField(source='first_name')
    lastname = serializers.CharField(source='last_name')
    created = serializers.CharField(source='date_joined')
    avatar_img_path = serializers.CharField(source='avatar_url')

    class Meta:
        model = Contact
        # fields = ('id', 'first_name', 'last_name', 'date_joined', 'location', 'project')
        fields = ('id', 'name', 'lastname', 'created', 'avatar_img_path',  'location', 'project')
        depth = 1


class ContactsFilter(django_filters.FilterSet):
    class Meta:
        model = Contact
        fields = ('id', 'first_name', 'last_name', 'date_joined', 'location', 'project')


class ContactsViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ContactsFilter
