from django.urls import path 
from . import views

urlpatterns = [
    path('contact/', views.contact_view, name='contact'),
    path('messages/', views.message_list, name='message_list'),
    path('messages/<int:message_id>/', views.message_detail, name='message_detail'),
]