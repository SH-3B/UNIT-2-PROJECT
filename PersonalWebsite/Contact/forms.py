from django import forms
from .models import ContactMessage

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject','category','message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your message here...'})
        }
class ContactMessageReplyForm(forms.Form):
    reply = forms.CharField(widget=forms.Textarea(attrs={'rows': 6, 'cols': 50}), label="Your Reply")
    
class MessageFilterForm(forms.Form):
    category = forms.ChoiceField(
        choices=[('', 'All Categories')] + ContactMessage.CATEGORY_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )