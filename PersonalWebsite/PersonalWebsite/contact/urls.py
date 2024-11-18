from django.urls import path 
from . import views
app_name = 'contact'
urlpatterns = [
    path('contact/', views.contact_view, name='contact'),
    path('messages/', views.message_list, name='message_list'),
    path('messages/<int:message_id>/', views.reply_to_message, name='message_detail'),
]