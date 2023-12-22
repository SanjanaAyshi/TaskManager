from django import forms
from .models import Tasks


class TaskFrom(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'
