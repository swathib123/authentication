from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Authenication, SupervisorAuthenication
from .serializers import userserializers,supervisorserializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET','POST'])
def custommanager(request):
    if request.method == 'GET':
        user = Authenication.objects.all()
        serializer = userserializers(user, many=True)
        return JsonResponse({'managerlist':serializer.data})

    if request.method == 'POST':
        serializer = userserializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)    

@api_view(['GET','PUT','DELETE'])
def manager_id(request,id):
    user = Authenication.objects.get(pk = id)
    if request.method == 'GET':
        serializer = userserializers(user)
        return Response(serializer.data)
    
    elif request.method=='PUT':
        serializer = userserializers(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
         user.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)
    



@api_view(['GET','POST'])
def customsupervisor(request):
    if request.method == 'GET':
        user = SupervisorAuthenication.objects.all()
        serializer = supervisorserializers(user, many=True)
        return JsonResponse({'supervisorlist':serializer.data})

    if request.method == 'POST':
        serializer = supervisorserializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)    

@api_view(['GET','PUT','DELETE'])
def supervisor_id(request,id):
    user = SupervisorAuthenication.objects.get(pk = id)
    if request.method == 'GET':
        serializer = supervisorserializers(user)
        return Response(serializer.data)
    
    elif request.method=='PUT':
        serializer = supervisorserializers(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
         user.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)


