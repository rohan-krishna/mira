from django.urls import path
from . import views


app_name='tasks_react'

urlpatterns=[
    path('',views.index, name='index'),
    path('api/tasks/', views.TaskList.as_view(), name='api_tasks'),
]