from .models import UserModel
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id','first_name', 'last_name', 'email', 'middle_name')
