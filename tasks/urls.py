from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns=[
    path('',views.index, name='index'),
    path('all-tasks',views.allTasks, name='all-tasks'),
    path('mark-task-complete/<int:pk>',views.markTaskComplete, name='mark-task-complete'),
    path('add-new-task',views.addNewTask, name='add'),
    path('delete-task/<int:pk>', views.deleteTask, name="delete-task"),
    path('show-task/<int:pk>', views.showTask, name="show-task"),
]