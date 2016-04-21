from rest_framework import serializers

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