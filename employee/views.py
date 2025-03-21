from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, LeaveRequest, Attendance, Payroll
from .forms import EmployeeForm, LeaveRequestForm, AttendanceForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils import timezone

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def employee_add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.user = request.user  # Automatically assign the current user
            employee.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form})

def employee_edit(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_form.html', {'form': form})

def leave_request_list(request):
    leave_requests = LeaveRequest.objects.all()
    return render(request, 'leave_request_list.html', {'leave_requests': leave_requests})

def leave_request_add(request):
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leave_request_list')
    else:
        form = LeaveRequestForm()
    return render(request, 'leave_request_form.html', {'form': form})

def attendance_page(request):
    employees = Employee.objects.all()
    return render(request, 'attendance_page.html', {'employees': employees})

current_employee = None  

def check_in(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            employee = form.cleaned_data['employee_id']

            # Check if the employee has already checked in
            attendance, created = Attendance.objects.get_or_create(
                employee=employee,
                date=timezone.now().date()
            )

            if not attendance.check_in:
                attendance.check_in = timezone.now()
                attendance.save()

    return redirect('attendance_page')

def check_out(request):
    global current_employee
    if current_employee:
        attendance = Attendance.objects.filter(
            employee=current_employee,
            check_out__isnull=True
        ).first()

        if attendance:
            attendance.check_out = timezone.now()
            attendance.save()
            Employee.objects.filter(id=current_employee.id).update(attendance_status='Checked Out')  

        current_employee = None 

    return redirect('attendance_page')

def payroll(request):
    payrolls = Payroll.objects.select_related('employee').all() 
    return render(request, 'payroll.html', {'payrolls': payrolls})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('attendance_page')
        else:
            return render(request, 'login.html', {'error': 'Invalid Credentials'})

    return render(request, 'login.html')
