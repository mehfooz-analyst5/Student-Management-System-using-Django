from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import User, Staff


# Create your views here.
login_required(login_url='login')
def ShowPage(request):
    return render(request, 'student_management_app/index.html')


def ShowLoginPage(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(f"Email: {email}, Password: {password}")
        
        try:
            user = get_user_model.objects.get(email=email)
            print(f"User: {user}")

        except:
            messages.error(request, "User doest not exist.")

        user = authenticate(request, username=email, password=password)
        print(f"Authenticated User: {user}")
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Email & Password doest not exist.")

    return render(request, 'student_management_app/login.html')


def Logoutpage(request):
    logout(request)
    return redirect('login')




#---------------- HOD Views ------------------------------
# Create your views here.
login_required(login_url='login')
def HodPageView(request):
    return render(request, 'student_management_app/hod_template/home-content.html')


login_required(login_url='login')
def addStaff(request):

    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')

        try:
            user = User.objects.create(
            name=name,
            email=email,
            password=password,
            user_type=2
            )

            user.staff.address=address
            user.save()
            messages.success(request, "Successfully Added Staff.")
            return redirect('add-staff')

        except :
            print('going to except')
            messages.error(request, "Failed to add Staff.")
            return redirect('add-staff')

    return render(request, 'student_management_app/hod_template/add_staff.html')
