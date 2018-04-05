from django import forms
from .models import *

RECURRING_TYPES=(
    ('daily','Daily'),
    ('once','Once'),
)

class TaskForm(forms.ModelForm):
    recurring_type = forms.ChoiceField(choices=RECURRING_TYPES, required=True)
    class Meta:
        model=Task
        fields = '__all__'
        exclude= ('owner','is_full_day_task','is_recurring','start_date','end_date','start_time','end_time')