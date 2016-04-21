from rest_framework import serializers

from models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'alias', 'active')

    def __unicode__(self):
        return self.name

    def create(self, validated_data):
        company = Company(
            name=validated_data['name'],
            alias=validated_data['name'].lower(),
            active=validated_data['active']
        )
        company.save()
        return company

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.alias = validated_data.get('name', instance.name).lower()
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance
