import django_filters

from rest_framework import routers, serializers, viewsets, filters

from common.common import StandardResultsSetPagination
from apps.contacts.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='first_name')
    lastname = serializers.CharField(source='last_name')
    created = serializers.CharField(source='date_joined')
    avatar_img_path = serializers.CharField(source='avatar_url')

    class Meta:
        model = Contact
        fields = ('id', 'name', 'lastname', 'created', 'avatar_img_path',  'location')
        depth = 1


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
