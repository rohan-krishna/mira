from datetime import date
from django import forms
from .models import *

RECURRING_TYPES=(
    ('daily','Daily'),
    ('once','Once'),
)

class TaskForm(forms.ModelForm):
    recurring_type = forms.ChoiceField(choices=RECURRING_TYPES, required=True)
    name = forms.CharField(required=True)
    
    class Meta:
        model=Task
        fields = '__all__'
        exclude= ('owner','is_full_day_task','is_recurring','start_date','end_date','start_time','end_time')


class UserProfileInfoForm(forms.ModelForm):
    model = UserProfileInfo
    fields = ('portfolio_site','profile_pic')