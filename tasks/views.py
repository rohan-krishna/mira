import calendar
import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from calendar import HTMLCalendar


# Create your views here.
def index(request):
    tasks = Task.objects.all()
    context = { 
        'tasks': tasks, 
        'daysInMonth' : range(calendar.monthrange(datetime.datetime.now().year, datetime.datetime.now().month)[1]), 
        'calendar': HTMLCalendar(calendar.SUNDAY)
        }
    return render(request, "tasks/index.html", context)
