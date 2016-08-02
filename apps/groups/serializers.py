from rest_framework import serializers

from models import Group


class GroupsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'name', 'admin', 'active')

    def __unicode__(self):
        return self.name
