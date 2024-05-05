# forms.py
from django import forms
from .models import Project
from django.utils import timezone

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'title',
            'price',
            'description',
            'deadline',
            ]
        widgets = {
            'deadline': forms.DateInput(
                attrs={
                    'type': 'date',
                    'min': timezone.now().date()
                }
            )
        }
