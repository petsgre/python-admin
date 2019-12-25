from quickstart.models import User, Test
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'created', 'phone', 'password',)


class TestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Test
        fields = ('id', 'content')
