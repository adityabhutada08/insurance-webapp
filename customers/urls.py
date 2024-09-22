from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_customer, name='add_customer'),
    path('add_family/', views.add_family_member, name='add_family_member'),
       
]
