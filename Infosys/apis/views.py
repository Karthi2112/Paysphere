from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from apis.forms import CustomUserCreationForm  
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer
from apis.forms import EmployeeForm
from django.http import HttpResponse
from datetime import datetime
from django.contrib import messages
from django.db import IntegrityError
from apis.models import LeaveRequest
from apis.forms import LeaveRequestForm
from django.http import HttpResponseForbidden
from django import template
from apis.utils import send_email_notification
from django.contrib.auth.models import User
from apis.models import CustomUser




class EmployeeCreateView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

def home(request):
    employees = Employee.objects.all()
    return render(request, 'home.html', {'employees': employees})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.role = form.cleaned_data['role'] 
            user.save()
            login(request, user)  
            messages.success(request, "Registration successful.")
            print(user)
            return redirect('home')  

        else:
            messages.error(request, "Error in registration. Please try again.")
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})
@login_required
def add_employee(request):
    if request.user.role in ['HR', 'Manager']: 
        if request.method == "POST":

            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            role = request.POST.get('role')  
            hourly_rate = request.POST.get('hourly_rate')
            
            if first_name and last_name and email and phone and role and hourly_rate:
                employee = Employee(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    phone=phone,
                    role=role,
                    hourly_rate=hourly_rate
                )
                employee.save()
                return redirect('home')  
            else:
                messages.error(request, "Please fill in all fields.")
        return render(request, 'add_employee.html')
    else:
        return redirect('home')  

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            if user.role == 'HR' or user.role == 'Manager':
                return redirect('home')  
            else:
                return redirect('home')  
        else:
            messages.error(request, 'Invalid credentials')
            return render(request, 'login.html')
    
    return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def logged_in_users(request):
    users = User.objects.filter(last_login__isnull=False)
    return render(request, 'logged_in_users.html', {'users': users})

@login_required
def employee_list(request):
    users = CustomUser.objects.all()
    return render(request, 'employee_list.html', {'users': users})

@login_required
def employee_detail(request, employee_id):
    employees = Employee.objects.filter(role__in=['Developer', 'Software Engineer'])
    return render(request, 'employee_profile.html', {'employees': employees})



@login_required
def employee_edit(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        employee.first_name = request.POST.get('first_name')
        employee.last_name = request.POST.get('last_name')
        employee.email = request.POST.get('email')
        employee.phone = request.POST.get('phone')
        employee.role = request.POST.get('role')
        employee.status = request.POST.get('status')
        employee.hourly_rate = request.POST.get('hourly_rate')
        date_joined = request.POST.get('date_joined')
        employee.date_joined = date_joined if date_joined else datetime.now().date()
        employee.save()
        return redirect('home')
    return render(request, 'employee_edit.html', {'employee': employee})

@login_required
def update_profile(request):
    if request.method == 'POST':
        user = request.user  # Get the logged-in user object
        user.first_name = request.POST.get('firstname')  # Use the correct key from the form
        user.last_name = request.POST.get('lastname')    # Use the correct key from the form
        user.email = request.POST.get('email')
        user.phone = request.POST.get('phone')
        
        # Ensure no required fields are empty
        if not user.first_name or not user.last_name or not user.email or not user.phone:
            from django.contrib import messages
            messages.error(request, "All fields are required!")
            return render(request, 'employee_profile.html', {'user': user})
        
        user.save()  # Save changes to the database
        return redirect('home')  # Redirect to home page after update
    return render(request, 'employee_profile.html', {'user': request.user})

def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    employee.delete()
    return redirect('home')  

def generate_payroll(request):
    return redirect("generate_payroll.html")


@login_required
def leave_requests(request):
    leave_requests = LeaveRequest.objects.all()  
    return render(request, 'leave_requests.html', {'leave_requests': leave_requests})
@login_required
def create_leave_request(request):
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            leave_request = form.save(commit=False)
            leave_request.employee = request.user  
            leave_request.status = 'Pending' 
            leave_request.save()
            return redirect('leave_list')
    else:
        form = LeaveRequestForm()

    return render(request, 'leave_request_form.html', {'form': form})

@login_required
def approve_leave_request(request, leave_request_id):
    leave_request = LeaveRequest.objects.get(id=leave_request_id)
    leave_request.status = 'Approved'
    leave_request.save()

    # Send notification email
    subject = "Leave Request Approved"
    message = (
        f"Dear {leave_request.employee.first_name},\n\n"
        f"Your leave request from {leave_request.start_date} to {leave_request.end_date} "
        f"has been approved by HR.\n\n"
        "Best regards,\nHR Team"
    )
    recipient_email = leave_request.employee.email
    send_email_notification(subject, message, recipient_email)
    return redirect('leave_requests')

@login_required
def reject_leave_request(request, leave_request_id):
    leave_request = LeaveRequest.objects.get(id=leave_request_id)
    leave_request.status = 'Rejected'
    leave_request.save()

    subject = "Leave Request Rejected"
    message = (
        f"Dear {leave_request.employee.first_name},\n\n"
        f"Unfortunately, your leave request from {leave_request.start_date} to {leave_request.end_date} "
        f"has been rejected by HR.\n\n"
        "Best regards,\nHR Team"
    )
    recipient_email = leave_request.employee.email
    send_email_notification(subject, message, recipient_email)

    return redirect('leave_requests')


@login_required
def leave_list(request):
    leave_requests = LeaveRequest.objects.filter(employee=request.user)
    return render(request, 'leave_list.html', {'leave_requests': leave_requests})

@login_required
def update_leave_request(request, leave_request_id):
    leave_request = get_object_or_404(LeaveRequest, id=leave_request_id)
    
    if request.user != leave_request.employee:
        return HttpResponseForbidden("You cannot edit this leave request.")

    if request.method == 'POST':
        form = LeaveRequestForm(request.POST, instance=leave_request)
        if form.is_valid():
            form.save()
            return redirect('leave_requests')  # Redirect after saving the updated leave request
    else:
        form = LeaveRequestForm(instance=leave_request)

    return render(request, 'update_leave_request.html', {'form': form, 'leave_request': leave_request})

@login_required
def delete_leave_request(request, leave_request_id):
    leave_request = get_object_or_404(LeaveRequest, id=leave_request_id)
    
    # Ensure the user is the owner of the leave request
    if request.user != leave_request.employee:
        return HttpResponseForbidden("You cannot delete this leave request.")

    leave_request.delete()  # Delete the leave request
    return redirect('leave_requests') 

@login_required
def review_leave_requests(request, leave_request_id):
    leave_request = get_object_or_404(LeaveRequest, id=leave_request_id)

    if request.user.role in ['HR', 'Manager']:
        leave_request = LeaveRequest.objects.get(id=leave_request_id)
        if request.method == 'POST':
            status = request.POST.get('status')
            if status in ['Approved', 'Rejected']:
                leave_request.status = status
                leave_request.save()
                return redirect('home')  # After review, go back to manager dashboard
        return render(request, 'review_leave_request.html', {'leave_request': leave_request})
    else:
        return redirect('home')  # Unauthorized access handling for employees