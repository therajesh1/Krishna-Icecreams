from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name='index'),
    path('dashboard',views.index,name='dashboard'),
    path('about',views.about,name='about'),
    path('services',views.services,name='service'),
    path('contact',views.contact,name='contact'),
    path('sign',views.sign,name='sign'),
    path('logout',views.logout,name='logout'),
    path('proceed',views.logout,name='proceed'),
]
