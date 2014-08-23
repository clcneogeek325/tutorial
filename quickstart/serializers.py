from django.contrib.auth.models import User, Group
from rest_framework import serializers
from quickstart.models import alumno

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class AlumnoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = alumno
		fields = ('id','nombre','apellidos','edad','status')
	
