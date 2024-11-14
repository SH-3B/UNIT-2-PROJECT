from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
     path('', views.dashboard_home, name='dashboard_home'),
    
    # Education URLs
    path('education/', views.education_list, name='education_list'),
    path('education/add/', views.add_education, name='add_education'),
    path('education/edit/<int:pk>/', views.update_education, name='update_education'),
    path('education/delete/<int:pk>/', views.delete_education, name='delete_education'),

    # Interest URLs
    path('interest/', views.interest_list, name='interest_list'),
    path('interest/add/', views.add_interest, name='add_interest'),
    path('interest/edit/<int:pk>/', views.update_interest, name='update_interest'),
    path('interest/delete/<int:pk>/', views.delete_interest, name='delete_interest'),

    # Service URLs
    path('service/', views.service_list, name='service_list'),
    path('service/add/', views.add_service, name='add_service'),
    path('service/edit/<int:pk>/', views.update_service, name='update_service'),
    path('service/delete/<int:pk>/', views.delete_service, name='delete_service'),
]
