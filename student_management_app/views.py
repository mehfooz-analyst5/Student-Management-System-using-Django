from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import User, Staff, Course, Student, Subject
from django.shortcuts import get_object_or_404


# Create your views here.
login_required(login_url='login')
def ShowPage(request):
    return render(request, 'student_management_app/index.html')


def ShowLoginPage(request):

    # if request.user.is_authenticated:
    #     return redirect('home')

    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(f"Email: {email}, Password: {password}")
        
        try:
            user = User.objects.get(email__iexact=email)
            print(f"User: {user}")

        except:
            messages.error(request, "User doest not exist.")

        # user = authenticate(request, email=email, password=password)
        # print(f"Authenticated User: {user}")
        if user.password == password or authenticate(request, email=email, password=password):
            
            if user is not None:
                login(request, user)

                if user.user_type=='1':
                    return redirect('hod-admin')
                
                elif user.user_type=='2':
                    return HttpResponse('Staff Login')
                
                else:
                    return HttpResponse('Student Login'+str(user.user_type))       
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




login_required(login_url='login')
def addCourse(request):

    if request.method=='POST':
        course = request.POST.get('course')

        try:
            course = Course(course_name=course)
            course.save()
            messages.success(request, "Successfully Added Course.")
            return redirect('add-course')

        except :
            print('going to except')
            messages.error(request, "Failed to add Course.")
            return redirect('add-course')

    return render(request, 'student_management_app/hod_template/add_course.html')



login_required(login_url='login')
def addStudent(request):
    courses =  Course.objects.all()
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        course = request.POST.get('course')
        gender = request.POST.get('sex')
        session_start = request.POST.get('session_start')
        session_end = request.POST.get('session_end')


        try:
            user = User.objects.create(name=name, email=email, password=password, user_type=3)
            user.student.address=address
            course = Course.objects.get(id=course)
            user.student.course_id=course
            user.student.session_start_year=session_start
            user.student.session_end_year=session_end
            user.student.gender=gender
            user.student.profile_pic=""
            user.save()
            messages.success(request, "Successfully Added Student .")
            return redirect('add-student')

        except :
            print('going to except')
            messages.error(request, "Failed to add Student.")
            return redirect('add-student')

    return render(request, 'student_management_app/hod_template/add_student.html', {'courses':courses})



login_required(login_url='login')
def addSubject(request):
    courses =  Course.objects.all()
    staff = User.objects.filter(user_type=2)

    if request.method=='POST':
        subject = request.POST.get('subject')

        course_id = request.POST.get('course')
        course = Course.objects.get(id=course_id)

        staff_id = request.POST.get('staff')
        staff = User.objects.get(id=staff_id)

        print(f'Details : {subject}, {course}, {staff}')

        try:
            subject = Subject(subject_name=subject, course_id=course, staff_id=staff)
            subject.save()
            messages.success(request, "Successfully Added Subject.")
            return redirect('add-subject')

        except :
            print('going to except')
            messages.error(request, "Failed to add Subject.")
            return redirect('add-subject')
        
    context = {
        'courses' : courses,
        'staff' : staff,
    }


    return render(request, 'student_management_app/hod_template/add_subject.html', context)



# Create your views here.
login_required(login_url='login')
def manageStaff(request):
    staffs = Staff.objects.all()
    context = {
        'staffs' : staffs,
        }
    return render(request, 'student_management_app/hod_template/manage_staff.html', context)



# Create your views here.
login_required(login_url='login')
def manageStudent(request):
    students = Student.objects.all()
    context = {
        'students' : students,
        }
    return render(request, 'student_management_app/hod_template/manage-student.html', context)


# Create your views here.
login_required(login_url='login')
def manageCourse(request):
    courses = Course.objects.all()
    context = {
        'courses' : courses,
        }
    return render(request, 'student_management_app/hod_template/manage_course.html', context)


# Create your views here.
login_required(login_url='login')
def manageSubject(request):
    subjects = Subject.objects.all()
    context = {
        'subjects' : subjects,
        }
    return render(request, 'student_management_app/hod_template/manage_subject.html', context)





def updateStaff(request, staff_id):
    staff = get_object_or_404(Staff, id=staff_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')

        try:
            user = User.objects.get(id=staff.admin.id)
            user.name = name
            user.email = email
            user.save()

            staff.address = address
            staff.save()

            messages.success(request, "Successfully Updated Staff.")
            return redirect('/manage-staff')

        except Exception as e:
            print('Exception:', str(e))
            messages.error(request, "Failed to Update Staff.")
            return redirect('/update-staff/' + str(staff_id))
        

    context = {'staff': staff}

    return render(request, 'student_management_app/hod_template/update_staff.html', context)


@login_required(login_url='login')
def updateStudent(request, student_id):
    courses = Course.objects.all()
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        course_id = request.POST.get('course')
        gender = request.POST.get('sex')
        session_start = request.POST.get('session_start')
        session_end = request.POST.get('session_end')
        print('Details:', name, email, address, course_id, gender, session_start, session_end)

        try:
            user = User.objects.get(id=student.admin.id)
            print(user)
            user.name = name
            user.email = email
            user.save()
            print('User Updated', user.name, user.email)

            student.address = address
            student.session_start_year = session_start
            student.session_end_year = session_end
            student.gender = gender
            student.save()
            print('Student Updated', student.address, student.session_start_year, student.session_end_year, student.gender)

            course = get_object_or_404(Course, id=course_id)
            student.course_id = course
            student.save()
            print('Student Updated', student.course_id)

            messages.success(request, "Successfully Updated Student.")
            return redirect('/update-student/' + str(student_id))

        except Exception as e:
            print('Exception:', str(e))
            messages.error(request, "Failed to Update Student.")
            return redirect('/update-student/' + str(student_id))

    context = {
        'student': student,
        'courses': courses,
    }

    return render(request, 'student_management_app/hod_template/update-student.html', context)