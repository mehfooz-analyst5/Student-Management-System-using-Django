from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [

     path('', views.ShowPage, name='home'),
     path('login/', views.ShowLoginPage, name='login'),
     path('logout/', views.Logoutpage, name='logout'),



     #-------------------------------- HOD Views ----------------------

     path('hod-admin/', views.HodPageView, name='hod-admin'),

     path('add-staff/', views.addStaff, name='add-staff'),
     path('manage-staff/', views.manageStaff, name='manage-staff'),
     path('update-staff/<str:staff_id>/', views.updateStaff, name='update-staff'),


     path('add-course/', views.addCourse, name='add-course'),
     path('manage-course/', views.manageCourse, name='manage-course'),
     path('update-course/<str:course_id>/', views.updateCourse, name='update-course'),

     path('add-student/', views.addStudent, name='add-student'),
     path('manage-student/', views.manageStudent, name='manage-student'),
     path('update-student/<str:student_id>/', views.updateStudent, name='update-student'),

     path('add-subject/', views.addSubject, name='add-subject'),
     path('manage-subject/', views.manageSubject, name='manage-subject'),
     path('update-subject/<str:subject_id>/', views.updateSubject, name='update-subject'),



     #-------------------------------- Staff Views ------------------------------------------
     path('staff-admin/', views.staffAdmin, name='staff-admin'),



     #-------------------------------- Student Views ------------------------------------------
     path('student-home/', views.studentHome, name='student-home'),
] 