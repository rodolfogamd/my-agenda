from rest_framework import serializers

from models import MyContact


class MyContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyContact
        fields = ('id', 'user', 'contact', )

    def __unicode__(self):
        return "%s %s" % (self.user, self.contact)
