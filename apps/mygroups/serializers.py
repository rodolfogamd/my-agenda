from rest_framework import serializers

from models import MyGroups


class MyGroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyGroups
        fields = ('id', 'group', 'user')
