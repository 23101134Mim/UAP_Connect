from django import forms
from .models import ClassRoutine, Mark
from django import forms
from .models import ClassRoutine


class ClassRoutineForm(forms.ModelForm):
    class Meta:
        model = ClassRoutine
        fields = ['course', 'day', 'time', 'room']


class MarkForm(forms.ModelForm):
    class Meta:
        model = Mark
        fields = ['student', 'course', 'ct1', 'ct2', 'mid', 'final']