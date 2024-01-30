from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [

     path('', views.ShowPage, name='home'),
     path('login/', views.ShowLoginPage, name='login'),
     path('logout/', views.Logoutpage, name='logout'),

     #-------------------- HOD Views ---------------

     path('hod-admin/', views.HodPageView, name='hod-admin'),
     path('add-staff/', views.addStaff, name='add-staff'),

] 