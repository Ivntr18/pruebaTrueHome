from .models import propiedad
from rest_framework import serializers

class PropSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = propiedad
		fields = ('id','nombre','direccion','superficie','email')

class SigninSerializer(serializers.Serializer):
	username = serializers.CharField(required = True)
	password = serializers.CharField(required = True)

	
