from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import Education, Interest, Service
from .forms import EducationForm, InterestForm, ServiceForm

def dashboard_home(request):
    education_count = Education.objects.count()
    interest_count = Interest.objects.count()
    service_count = Service.objects.count()

    context = {
        'education_count': education_count,
        'interest_count': interest_count,
        'service_count': service_count,
    }

    return render(request, 'dashboard/dashboard_home.html', context)



def education_list(request):
    query = request.GET.get('q', '')
    educations = Education.objects.filter(
        Q(uni_name__icontains=query) | Q(description__icontains=query)
    ).order_by('graduation_year')

    return render(request, 'dashboard/education_list.html', {'educations': educations})


def add_education(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:education_list')
    else:
        form = EducationForm()

    return render(request, 'dashboard/add_education.html', {'form': form})


def update_education(request, pk):
    education = get_object_or_404(Education, pk=pk)
    
    if request.method == 'POST':
        form = EducationForm(request.POST,request.FILES, instance=education)
        if form.is_valid():
            form.save()
            return redirect('dashboard:education_list')
    else:
        form = EducationForm(instance=education)

    return render(request, 'dashboard/update_education.html', {'form': form, 'education': education})


def delete_education(request, pk):
    education = get_object_or_404(Education, pk=pk)
    if request.method == 'POST':
        education.delete()
        return redirect('dashboard:education_list')
    return render(request, 'dashboard/delete_education.html', {'education': education})



def interest_list(request):
    query = request.GET.get('q', '')
    interests = Interest.objects.all()
    search_query = request.GET.get('q', '')

   
    if search_query:
        interests = Interest.objects.filter(name__icontains=search_query) | Interest.objects.filter(quote__icontains=search_query)
    else:
        interests = Interest.objects.all()

    
    return render(request, 'dashboard/interest_list.html', {'interests': interests})


def add_interest(request):
    if request.method == 'POST':
        form = InterestForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()  
            return redirect('dashboard:interest_list') 
        else:
            print(form.errors)  
            return render(request, 'dashboard/add_interest.html', {'form': form})
    
    else:
        form = InterestForm() 

   
    return render(request, 'dashboard/add_interest.html', {'form': form})


def update_interest(request, pk):
    interest = get_object_or_404(Interest, pk=pk)

    if request.method == 'POST':
        form = InterestForm(request.POST, request.FILES, instance=interest)  

        if form.is_valid():
            form.save()  
            return redirect('dashboard:interest_list')  
        else:
            
            print(form.errors)
            return render(request, 'dashboard/update_interest.html', {'form': form})
    
  
    else:
        form = InterestForm(instance=interest) 

    return render(request, 'dashboard/update_interest.html', {'form': form})

def delete_interest(request, pk):
    interest = get_object_or_404(Interest, pk=pk)
    if request.method == 'POST':
        interest.delete()
        return redirect('dashboard:interest_list')
    return render(request, 'dashboard/delete_interest.html', {'interest': interest})

def service_list(request):
    query = request.GET.get('q', '')
    services = Service.objects.filter(
        Q(title__icontains=query) | Q(description__icontains=query)
    ).order_by('title')

    return render(request, 'dashboard/services_list.html', {'services': services})


def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:service_list')
    else:
        form = ServiceForm()

    return render(request, 'dashboard/add_services.html', {'form': form})


def update_service(request, pk):
    service = get_object_or_404(Service, pk=pk)
    
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('dashboard:service_list')
    else:
        form = ServiceForm(instance=service)

    return render(request, 'dashboard/update_service.html', {'form': form})


def delete_service(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        service.delete()
        return redirect('dashboard:service_list')
    return render(request, 'dashboard/delete_service.html', {'service': service})
