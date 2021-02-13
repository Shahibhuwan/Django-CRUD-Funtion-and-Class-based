from rest_framework import serializers
from .models import Task
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer

# Create your views here.

@api_view(['GET'])
def apiOverView(request):
    api_urls={
        'List':' /task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create' : '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>',
        }
    return Response(api_urls)

@api_view(['GET'])
def tasklist(request):
    tasks= Task.objects.all()                              #many=true menas we want to serialize many modelobject and false means we want to serialize single object
    serializer = TaskSerializer(tasks, many=True)      #serializer convert modelobject into python dict then json render converts it into json data
    return Response(serializer.data)


@api_view(['GET'])
def taskdetail(request, id):
    task= Task.objects.get(id= id)                              #many=true menas we want to serialize many modelobject and false means we want to serialize single object
    serializer = TaskSerializer(task, many=False)      #serializer convert modelobject into python dict then json render converts it into json data
    return Response(serializer.data)

@api_view(['POST'])
def taskcreate(request):
                             
    serializer = TaskSerializer(data= request.data)  #request.data is similar to request.post where request.data sends dict object whereas request.data sends json object
                                                             #serializer convert modelobject into python dict then json render converts it into json data
    if serializer.is_valid():                                      #similar to form.isvalid
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def taskupdate(request, id):
    task= Task.objects.get(id= id)                              #many=true menas we want to serialize many modelobject and false means we want to serialize single object
    serializer = TaskSerializer(instance=task, data=request.data)      #serializer convert modelobject into python dict then json render converts it into json data
    if serializer.is_valid():                                      #similar to form.isvalid
        serializer.save()
    return Response(serializer.data) #serializer.data sends data in json format

@api_view(['DELETE'])
def taskdelete(request, id):
    task =Task.objects.get(id =id)
    serializer = TaskSerializer(task, many=False)
    task.delete()
    return Response(serializer.data)


