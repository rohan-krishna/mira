import datetime
import sweetify
from itertools import chain

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from calendar import HTMLCalendar
from django.db import transaction
from django.contrib.auth.decorators import login_required

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *

from django.utils import timezone

from .forms import TaskForm
from . import helpers

# Create your views here.
@login_required
def index(request):

    dailyTasks = Task.objects.filter(
        owner=request.user,
        recurring_pattern__recurring_type="daily",
        start_date__lte=timezone.now().date()
    )

    onceTasks = Task.objects.filter(
        owner=request.user,
        recurring_pattern__recurring_type="once",
        start_date=timezone.now().date()
    )
    
    future_tasks = Task.objects.filter(
        owner=request.user,
        start_date__gt = timezone.now().date())

    combined_tasks = list(chain(dailyTasks,onceTasks))

    context = { 
        'future_tasks' : future_tasks,
        'combined_tasks' : combined_tasks
        }
    return render(request, "tasks/index.html", context)

@api_view(['GET'])
def allTasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@login_required
@transaction.atomic
def markTaskComplete(request, pk):
    
    if request.method == 'POST':
        t = Task.objects.get(pk=pk)

        # let's search for today's records
        record = t.records.filter(
            created_at__date=timezone.now()
        ).first()

        if not record:
            r = TaskRecord(task=t,is_completed=True,data=t)
            r.save()
        else:
            record.is_completed = True if not record.is_completed else False
            record.save()
        
        sweetify.success(request, 'Heads Up!.',text='The task\'s status has been toggled!', persistent="Noice!")
        
        return redirect('tasks:index')

    return redirect('tasks:index')

@login_required
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
            
            if request.POST['start_date']:
                task.start_date = datetime.datetime.strptime(request.POST['start_date'], "%m/%d/%Y").date()
            else:
                task.start_date = timezone.now().date()

            task.save()
            rp = RecurringPattern(recurring_type=request.POST['recurring_type'],task=task)
            rp.save()
            
            sweetify.success(request, 'The task has been successfully added.',persistent="Cool!")

            return redirect('tasks:index')
    return redirect('tasks:index')

@login_required
@transaction.atomic
def deleteTask(request,pk):
    t = Task.objects.get(pk=pk)
    t.delete()

    sweetify.info(request, 'The task has been successfully deleted.', persistent="All Righty!")
    return redirect('tasks:index')

@login_required
def showTask(request, pk):
    
    t = request.user.owner.get(pk=pk)

    dateslist = []
    records_count = 0
    efficiency = 0

    if t.recurring_pattern.recurring_type == 'daily':
    
        start_date = t.start_date
        end_date = timezone.now().date()

        for dt in helpers.daterange(start_date, end_date):
            
            r = t.records.filter(created_at__year=dt.year, created_at__month=dt.month, created_at__day=dt.day,is_completed=True)

            if r:
                dateslist.append({"date" : dt, "record" : r.first })
                records_count = records_count+1
            else:
                dateslist.append({"date" : dt})

        efficiency =  (records_count / len(dateslist) ) * 100
    
    else:
        
        start_date = t.start_date
        end_date = t.start_date

        for dt in helpers.daterange(start_date, end_date):
            
            r = t.records.filter(created_at__year=dt.year, created_at__month=dt.month,created_at__day=dt.day, is_completed=True)

            if r:
                dateslist.append({"date" : dt, "record" : r.first })
                records_count = records_count+1
            else:
                dateslist.append({"date" : dt})

        efficiency = (records_count / len(dateslist)) * 100


    context = {'task': t, 'dateslist' : dateslist, 'efficiency' : efficiency }

    return render(request, 'tasks/show.html', context)
