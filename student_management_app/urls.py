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
     path('manage-staff/', views.manageStaff, name='manage-staff'),


     path('add-course/', views.addCourse, name='add-course'),
     path('manage-course/', views.manageCourse, name='manage-course'),

     path('add-student/', views.addStudent, name='add-student'),
     path('manage-student/', views.manageStudent, name='manage-student'),

     path('add-subject/', views.addSubject, name='add-subject'),
     path('manage-subject/', views.manageSubject, name='manage-subject'),
] 