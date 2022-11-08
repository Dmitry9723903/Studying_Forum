import logging

from unittest import result
from django.forms import CharField
#from django.shortcuts import render

from rest_framework import viewsets
from api import serializers
from api.models import Checkbox
from api.serializers import CheckboxSerializer, DataSerializer
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import authentication, permissions
from rest_framework import generics, mixins
from api.utils import Sum

logger = logging.getLogger('django')

class CheckboxViewSet(viewsets.ModelViewSet):
    queryset = Checkbox.objects.all()
    serializer_class = CheckboxSerializer
    
    @action(detail=False, methods=["get"])
    def limit(self, req, pk=None):
        try:
            params = req.query_params
        except:
            logger.info('Params: %s', params)
        return Response({"result":params})

class CheckboxList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Checkbox.objects.all()
    serializer_class = CheckboxSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

#class CheckboxDetailed(APIView):
    #permission_classes = [permissions.IsAdminUser]

    #def get(self, req, pk, format = None):
        #checkbox = Checkbox.objects.get(id=pk)
        #checkbox.delete()
        #return Response(status = status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def checkbox_list(req):
    checkboxes = Checkbox.objects.all()
    serializer = CheckboxSerializer(checkboxes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def checkbox_detail(req, pk):
    try:
        checkbox = Checkbox.objects.get(id=pk)
        serializer = CheckboxSerializer(checkbox)
    except Checkbox.DoesNotExist:
        return Response((f"error: Checkbox with id = {pk} is not found"), status = status.HTTP_404_NOT_FOUND)
    return Response(serializer.data)

@api_view(['POST'])
def checkbox_create(req):
    serializer = CheckboxSerializer(data=req.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['PUT'])
def checkbox_update(req, pk):
    try:
        checkbox = Checkbox.objects.get(id=pk)
        serializer = CheckboxSerializer(checkbox, data=req.data)
        if serializer.is_valid():
            serializer.save()
    except Checkbox.DoesNotExist:
        return Response((f"error: Checkbox with id = {pk} is not found"), status = status.HTTP_404_NOT_FOUND)
    return Response(serializer.data)

@api_view(['DELETE'])
def checkbox_delete(req, pk):
    checkbox = Checkbox.objects.get(id=pk)
    checkbox.delete()
    return Response(status = status.HTTP_404_NOT_FOUND)

class DataView(APIView):

    @staticmethod
    def get(req):
        serializer = DataSerializer(data=req.query_params)
        serializer.is_valid(raise_exception=True)
        params = serializer.validated_data
        return Response({'params':params}, status=status.HTTP_200_OK)
