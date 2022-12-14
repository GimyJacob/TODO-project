from .models import Task
from django import forms


class Task_form(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'priority', 'date']
