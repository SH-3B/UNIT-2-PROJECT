from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('education/', views.education_view, name='education'),
    path('services/', views.services_view, name='services'),
    path('interests/', views.interests_view, name='interests'),
]