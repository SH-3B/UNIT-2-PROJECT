from django.shortcuts import render , redirect
from dashboard.models import Interest , Education , Service
from django.core.paginator import Paginator
# Create your views here.

def home(request):
     education_list = Education.objects.all()
     services = Service.objects.all() 
     interests = Interest.objects.all()  

     return render(request, 'about_myself/home.html', {
        'education_list': education_list,
        'services': services,
        'interests': interests,
    })

def education_view(request): 
    education_list = Education.objects.all()
    return render(request, 'about_myself/education.html', {'education_list': education_list})


def services_view(request):
    services = Service.objects.all() 
    return render(request, 'about_myself/services.html', { 'services': services})


def interests_view(request):
    search_term = request.GET.get('q', '')  
    category_filter = request.GET.get('category', '')

    interests = Interest.objects.all()
    
    if search_term:
        interests = interests.filter(name__icontains=search_term) 
    if category_filter:
        interests = interests.filter(category=category_filter)


    paginator = Paginator(interests, 6)  
    page_number = request.GET.get('page') 
    page_obj = paginator.get_page(page_number)  

    categories = Interest.CATEGORY_CHOICES

    return render(request, 'about_myself/interests.html', {
        'page_obj': page_obj,
        'interests': interests,
        'categories': categories,
        'category_filter': category_filter,
    })

