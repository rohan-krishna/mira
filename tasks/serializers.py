from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email')

class RecurringPatternSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecurringPattern
        fields = '__all__'
        depth = 1

class TaskSerializer(serializers.ModelSerializer):

    owner = UserSerializer(User)

    class Meta:
        model = Task
        fields = ('id','recurring_pattern','name','start_date','end_date','start_time','end_time','created_at','updated_at','owner','records')
        depth = 1