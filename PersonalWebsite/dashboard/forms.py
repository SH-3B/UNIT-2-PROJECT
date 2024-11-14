from django import forms
from .models import Education, Interest, Service

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['uni_name', 'description', 'graduation_year']

class InterestForm(forms.ModelForm):
    class Meta:
        model = Interest
        fields = ['name', 'description','image']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'description']
