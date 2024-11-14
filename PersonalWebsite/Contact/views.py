from django.shortcuts import render , redirect , get_object_or_404
from django.contrib import messages
from .forms import ContactMessageForm
from .models import ContactMessage
from .forms import ContactMessageReplyForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            contact_message = form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
        else:
            messages.error(request, 'There was an error with your submission. Please try again.')
            return render(request, 'Contact/contact.html', {'form': form})
    else:
        form = ContactMessageForm()
    return render(request, 'Contact/contact.html', {'form': form})

def message_list(request):
    messages_list = ContactMessage.objects.all().order_by('-created_at')
    return render(request, 'Contact/message_list.html', {'messages': messages_list})

def message_detail(request, message_id):
    message = get_object_or_404(ContactMessage, id=message_id)
    if request.method == 'POST':
        form = ContactMessageReplyForm(request.POST)
        if form.is_valid():
            message.reply = form.cleaned_data['reply']
            message.is_responded = True
            message.save()
            return redirect('contact_messages')
    else:
        form = ContactMessageReplyForm()
    return render(request, 'Contact/message_detail.html', {'form': form, 'message': message})
