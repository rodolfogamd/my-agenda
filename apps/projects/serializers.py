from django.contrib.auth.models import User, Group
from rest_framework import serializers

from apps.clients.serializers import ClientSerializer
from models import Project


class ProjectSerializer(serializers.ModelSerializer):
    # client = ClientSerializer(read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'name', 'client', 'active')

    def __unicode__(self):
        return "%s" % self.name


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
