from django.shortcuts import render,HttpResponse,get_object_or_404

#from django.http import HttpResponse
from .models import Stud 
from django.shortcuts import redirect
from .forms import StudForm 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import time

def home(request):
    return render(request,'home.html')

def student_report(request):
    return render(request,'student_report.html')

def about_us(request):
    return render(request,'about_us.html')

def why_we(request):
    return render(request,'why_we.html')

def contact_us(request):
    return render(request,'contact_us.html')

def user_login(request):
    return render(request,'user_login.html')



@login_required
def add_student(request):
    if request.method == 'POST':
        form = StudForm(request.POST)
        if form.is_valid():
            form.save()  # Save to the database
            return redirect('student_list')  # Redirect to a list view after adding
    else:
        form = StudForm()
    
    return render(request, 'add_student.html', {'form': form})

@login_required
def student_list(request):
    allStuds = Stud.objects.all()
    return render(request, 'student_list.html', {'studs': allStuds})

@login_required
def Mark_sheet_register(request):
    allStuds = Stud.objects.all()
    return render(request, 'Mark_sheet_register.html', {'studs': allStuds})

@login_required
def edit_student(request, rollNumber):
    try:
        stud = Stud.objects.get(roll_number=rollNumber)
    except Stud.DoesNotExist:
        messages.error(request, f"Sorry, student with Roll Number {rollNumber} does not exist!!")
       
        return redirect('home')  # Or 'home'

    if request.method == "POST":
        form = StudForm(request.POST, instance=stud)
        if form.is_valid():
            form.save()
            messages.success(request, "Student details updated successfully.")
            return redirect("student_list")
    else:
        form = StudForm(instance=stud)

    return render(request, 'edit_student.html', {'form': form, 'Stud': stud})

from django.contrib import messages

@login_required
def delete_student(request, roll_number):
    try:
        stud = Stud.objects.get(roll_number=roll_number)
    except Stud.DoesNotExist:
        messages.error(request, f"Sorry, student with Roll Number {roll_number} does not exist.")
        return redirect('home')  # Or 'home'

    if request.method == 'POST':
        stud.delete()
        messages.success(request, f"Student with Roll Number {roll_number} deleted successfully.")
        return redirect('student_list')

    return render(request, 'delete_student.html', {'Stud': stud})


def about_us(request):
    return render(request,'about_us.html')



def contact_us(request):
    return render(request,'contact_us.html')


@login_required
def student_report(request, roll_number):
    try:
        student = Stud.objects.get(roll_number=roll_number)
    except Stud.DoesNotExist:
        messages.error(request, f"Sorry, student with Roll Number {roll_number} does not exist.")
        return redirect('home')  # Or student_list if that's more appropriate

    return render(request, 'student_report.html', {'student': student})

from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")

            # Redirect to the original URL after login (if any)
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials")

    else:
        # Show message if redirected due to @login_required
        if 'next' in request.GET:
            messages.info(request, "Please login to continue.")

    return render(request, 'login.html')


from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out. Please log in again to continue.")  # ✅ Show logout message
    return redirect('user_login')
