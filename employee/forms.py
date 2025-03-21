from django import forms
from .models import Employee, LeaveRequest

class EmployeeForm(forms.ModelForm):
   
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'department', 'position', 'hire_date', 'resignation_date']

class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ['employee', 'leave_type', 'start_date', 'end_date', 'reason']

class AttendanceForm(forms.Form):
    employee_id = forms.ModelChoiceField(
        queryset=Employee.objects.all(), 
        empty_label="Select Employee",
        label="Employee Name"  
    )
