# Create your views here.

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import propiedad
from .serializers import PropSerializer, SigninSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .authentication import token_expire_handler, expires_in
from django.contrib.auth import authenticate
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
)


class PropList(generics.ListCreateAPIView):
	queryset = propiedad.objects.all()
	serializer_class = PropSerializer
	#permission_classes = (IsAuthenticated,)

	def get_object(self):
		queryset = self.get_queryset()
		obj = get_object_or_404(queryset,pk=self.kwargs['pk'],) 
		return obj


class PropDetail(APIView):
	permission_classes = (IsAuthenticated,)
	def get(self, request, pk):
		new_token = Token.objects.create(user=request.user)
		obj=get_object_or_404(propiedad, pk=pk)
		serializer = PropSerializer(obj)
		return Response(serializer.data)

	def delete(self, request, pk):
		obj=get_object_or_404(propiedad, pk=pk)
		obj.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

	def post(self, request, format=None):
		serializer = PropSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status= status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def patch(self, request, pk):
		obj=get_object_or_404(propiedad, pk=pk)
		serializer = PropSerializer(obj,data = request.data, partial=True)

		if serializer.is_valid():
			serializer.save()

		return Response(serializer.data)

class Auth(APIView):
	def post(self,request, format=None):
		signin_serializer = SigninSerializer(data = request.data)
		if not signin_serializer.is_valid():
			return Response(signin_serializer.errors, status = HTTP_400_BAD_REQUEST)


		user = authenticate(
			username = signin_serializer.data['username'],
			password = signin_serializer.data['password'] 
		)
		if not user:
			return Response({'detail': 'Invalid Credentials or activate account'}, status=HTTP_404_NOT_FOUND)
        
		#TOKEN STUFF
		token, _ = Token.objects.get_or_create(user = user)
    
    #token_expire_handler will check, if the token is expired it will generate new one
		is_expired, token = token_expire_handler(token)     # The implementation will be described further
		#user_serialized = UserSerializer(user)

		return Response({
		'user': signin_serializer.data['username'], 
		'expires_in': expires_in(token),
		'token': token.key
		}, status=HTTP_200_OK)


