from django.shortcuts import render , redirect
from .models import Interest
from .forms import InterestForm
from .models import Education
from .forms import EducationForm
from .models import Service
from .forms import ServiceForm
# Create your views here.

def home(request):
     education_list = Education.objects.all()  # Get all education records
     services = Service.objects.all()  # Get all services
     interests = Interest.objects.all()  # Get all interests

     return render(request, 'AboutMyself/test.html', {
        'education_list': education_list,
        'services': services,
        'interests': interests,
    })

def education_view(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('education')  
    else:
        form = EducationForm()

   
    education_list = Education.objects.all()

    return render(request, 'AboutMyself/education.html', {'form': form, 'education_list': education_list})


def services_view(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('services') 
    else:
        form = ServiceForm()

    services = Service.objects.all() 
    return render(request, 'AboutMyself/services.html', {'form': form, 'services': services})

def interests_view(request):
    if request.method == 'POST':
        form = InterestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('interests')  
    else:
        form = InterestForm()

    interests = Interest.objects.all()  
    return render(request, 'AboutMyself/interests.html', {'form': form, 'interests': interests})