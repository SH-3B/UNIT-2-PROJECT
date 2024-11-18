from django.db import models
from django import forms

class ContactMessage(models.Model):
    CATEGORY_CHOICES = [
        ('services', 'Services'),
        ('feedback', 'Feedback'),
        ('questions', 'Questions'),
    ]
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='services')
    created_at = models.DateTimeField(auto_now_add=True)
    is_responded = models.BooleanField(default=False)
    reply = models.TextField(blank=True, null=True)  
    is_replied = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.subject} ({self.get_category_display()})"
    
class ContactMessageReplyForm(forms.Form):
    reply = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}), label="Your Reply")
