from django import forms
from .models import Education, Interest, Service

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['uni_name', 'description', 'graduation_year']
        labels = {
            'uni_name': 'Institution Name', 
            'description': 'Description',  
            'graduation_year': 'Year of Graduation',  
        }


class InterestForm(forms.ModelForm):
    class Meta:
        model = Interest
        fields = ['category', 'name', 'description', 'quote', 'meaning', 'why_chose', 'image']
        widgets = {
            'category': forms.Select(choices=Interest.CATEGORY_CHOICES),
        }

    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get('category')

        if category == 'drink' or category == 'city':
            meaning = cleaned_data.get('meaning')
            why_chose = cleaned_data.get('why_chose')

            if meaning and meaning.strip():
                raise forms.ValidationError("Field 'Meaning' should not be filled for this category.")
            if why_chose and why_chose.strip():
                raise forms.ValidationError("Field 'Why Chose' should not be filled for this category.")
        
        return cleaned_data

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'description']
