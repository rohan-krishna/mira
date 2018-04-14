import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=255, blank=True)
    owner = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    is_full_day_task = models.BooleanField(default=False)
    is_recurring = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class RecurringPattern(models.Model):
    task = models.OneToOneField(Task, related_name='recurring_pattern',on_delete=models.CASCADE)
    recurring_type = models.CharField(max_length=255, blank=True, null=True)
    separation_count = models.PositiveIntegerField(blank=True, null=True)
    max_number_of_occurences = models.IntegerField(blank=True, null=True)
    day_of_week = models.IntegerField(blank=True, null=True)
    day_of_month = models.IntegerField(blank=True, null=True)
    week_of_month = models.IntegerField(blank=True, null=True)
    month_of_year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.task.name + ":" + self.recurring_type

class TaskException(models.Model):
    task = models.ForeignKey(Task, related_name='exception_instance', on_delete=models.CASCADE)
    is_rescheduled = models.IntegerField(blank=True, null=True)
    is_cancelled = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    is_full_day_task = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)

class TaskRecord(models.Model):
    task = models.ForeignKey(Task, related_name='records', on_delete=models.CASCADE)
    data = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task.name + " (" + str(self.is_completed) + ") " 

class UserProfileInfo(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # additional
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)


    def __str__(self):
        return self.user.username

