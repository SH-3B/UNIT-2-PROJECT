from django import forms
from .models import Interest
from .models import Education
from .models import Service

class InterestForm(forms.ModelForm):
    class Meta:
        model = Interest
        fields = ['name', 'description', 'image']


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['uni_name', 'year', 'description']
        widgets = {
            'year': forms.NumberInput(attrs={'placeholder': 'e.g., 2024'}),
            'description': forms.Textarea(attrs={'placeholder': 'e.g., Description of your experience'}),
        }

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'description']