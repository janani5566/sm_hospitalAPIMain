from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from .serializers import subscribeSerializer,secondarySerializer
from rest_framework.viewsets import ModelViewSet
from .models import login,Secondary
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework import viewsets


from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET' ,'POST','PUT'])
def showexp(request,Id=0):
    if request.method == 'GET':
        results=login.objects.all()
        serialize = subscribeSerializer(results, many=True)
        return Response(serialize.data)
    elif request.method=='POST':
        serialize = subscribeSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='PUT':
        results = login.get_object()
        serialize = subscribeSerializer(results, data=request.data,many = True)
        if serialize.is_valid():
             serialize.save()
             return Response(serialize.data)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)


class loginView(viewsets.ModelViewSet):
    queryset = login.objects.all()
    serializer_class = subscribeSerializer

class SecondaryView(viewsets.ModelViewSet):
    queryset = Secondary.objects.all()
    serializer_class = secondarySerializer