from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='index'),
    path('services/', views.service, name='services'),
    path('Items/', views.item, name='item'),
    path('contact/', views.contact, name='contact'),
    path('bag/', views.bag, name='bag'),
]