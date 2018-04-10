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
    tasks = Task.objects.filter(
        owner=request.user,
        start_date = timezone.now())

    dailyTasks = Task.objects.filter(
        owner=request.user,
        recurring_pattern__recurring_type="daily"
    ).exclude(end_date__lt=timezone.now())

    onceTasks = Task.objects.filter(
        owner=request.user,
        recurring_pattern__recurring_type="once",
        start_date=timezone.now()
    )
    
    future_tasks = Task.objects.filter(
        owner=request.user,
        start_date__gt = timezone.now())

    context = { 
        'tasks': tasks, 
        'daysInMonth' : range(calendar.monthrange(datetime.datetime.now().year, datetime.datetime.now().month)[1]), 
        'calendar': HTMLCalendar(calendar.SUNDAY),
        'future_tasks' : future_tasks,
        'daily_tasks' : dailyTasks,
        'once_tasks' : onceTasks
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

        # let's search for today's records
        record = t.records.filter(
            created_at__day=timezone.now().day,
            created_at__month=timezone.now().month,
            created_at__year=timezone.now().year
        ).first()

        if not record:
            r = TaskRecord(task=t,is_completed=True,data=t)
            r.save()
        else:
            record.is_completed = True if not record.is_completed else False
            record.save()
        
        return redirect('tasks:index')

    return redirect('tasks:index')

@transaction.atomic
def addNewTask(request):
    form = TaskForm()
    
    if request.method == 'GET':
        return render(request, "tasks/add.html", {'form' : form})

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.start_date = timezone.now()
            task.save()
            rp = RecurringPattern(recurring_type=request.POST['recurring_type'],task=task)
            rp.save()

            return redirect('tasks:index')
    return redirect('tasks:index')
