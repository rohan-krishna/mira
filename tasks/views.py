import calendar
import datetime
import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from calendar import HTMLCalendar
from django.db import transaction

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *

from django.utils import timezone

from .forms import TaskForm

# Create your views here.
def index(request):
    tasks = Task.objects.filter(owner=request.user)
    context = { 
        'tasks': tasks, 
        'daysInMonth' : range(calendar.monthrange(datetime.datetime.now().year, datetime.datetime.now().month)[1]), 
        'calendar': HTMLCalendar(calendar.SUNDAY)
        }
    return render(request, "tasks/index.html", context)

@api_view(['GET'])
def allTasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@transaction.atomic
def markTaskComplete(request, pk):
    
    if request.method == 'POST':
        t = Task.objects.get(pk=pk)

        records = t.records.filter(created_at__day=timezone.now().day, created_at__month=timezone.now().month, created_at__year=timezone.now().year)
        
        if(records.count() <= 0): 
            r = TaskRecord(task=t,data=t)
            r.save()
        return redirect('tasks:index')
    else:
        return redirect('tasks:index')

    return redirect('tasks:index')

@transaction.atomic
def addNewTask(request):
    form = TaskForm()
    
    if request.method == 'GET':
        return render(request, "tasks/add.html", {'form' : form})

    if request.method == 'POST':
        task = TaskForm(request.POST)

        if task.is_valid():
            task.save()
