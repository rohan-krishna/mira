from django.shortcuts import render
from django.http import HttpResponse
from tasks.models import *
from .serializers import TaskSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

def index(request):
    return render(request, "tasks_react/index.html", {})

class TaskList(APIView):
    def get(self, request, format=None):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
