from django.shortcuts import render , redirect , get_object_or_404
from django.contrib import messages
from .forms import ContactMessageForm
from .models import ContactMessage
from django.conf import settings
from django.core.mail import send_mail
from .forms import ContactMessageReplyForm
from django.core.mail import EmailMessage


def contact_view(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            contact_message = form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact:contact')
        else:
            messages.error(request, 'There was an error with your submission. Please try again.')
            return render(request, 'contact/contact.html', {'form': form})
    else:
        form = ContactMessageForm()
    return render(request, 'contact/contact.html', {'form': form})

def message_list(request):
    category_filter = request.GET.get('category', '') 
    replied_filter = request.GET.get('replied', '')  

    messages = ContactMessage.objects.all()  

    if category_filter:
        messages = messages.filter(category=category_filter)

    if replied_filter == 'replied':
        messages = messages.filter(is_replied=True)
    elif replied_filter == 'not_replied':
        messages = messages.filter(is_replied=False)

    categories = ContactMessage.CATEGORY_CHOICES

    return render(request, 'contact/message_list.html', {
        'messages': messages,
        'categories': categories,
        'category_filter': category_filter,
        'replied_filter': replied_filter,  
    })

def reply_to_message(request, message_id):
    message = get_object_or_404(ContactMessage, id=message_id)
    
    replied = message.is_replied

    if request.method == 'POST':
        reply_message = request.POST.get('reply_message')

        subject = f"Re: {message.subject}"
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = message.email

        email_body = f"Dear {message.name},\n\n{reply_message}\n\n--\nOriginal Message:\n{message.message}"

        email = EmailMessage(
            subject=subject,
            body=email_body,
            from_email=from_email,
            to=[to_email],
        )

        try:
            email.send()
            messages.success(request, 'Your reply has been sent successfully.')

            message.is_replied = True
            message.save()

            replied = True  
        except Exception as e:
            messages.error(request, f"An error occurred while sending the reply: {str(e)}")

        return redirect('contact:message_list')   

    return render(request, 'contact/message_detail.html', {'message': message, 'replied': replied})