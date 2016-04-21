from rest_framework import serializers

from models import Groups


class GroupsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Groups
        fields = ('id', 'name', 'active')

    def __unicode__(self):
        return self.name
