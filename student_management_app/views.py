from django.shortcuts import render

# Create your views here.

def ShowPage(request):
    return render(request, 'student_management_app/index.html')
