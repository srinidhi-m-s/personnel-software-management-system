from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    hire_date = models.DateField() 
    resignation_date = models.DateField(null=True, blank=True)
    leave_balance = models.FloatField(default=20.0)
    attendance_status = models.CharField(max_length=10, default='Absent')

     # Payroll-related fields
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_working_days = models.IntegerField(default=0)
    leave_days = models.IntegerField(default=0)
    net_salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class LeaveRequest(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField() 
    reason = models.TextField()
    status = models.CharField(max_length=20, default='Pending')

    def save(self, *args, **kwargs):
        if self.status == 'Approved':
            leave_days = (self.end_date - self.start_date).days + 1
            self.employee.leave_balance -= leave_days
            self.employee.save()
        super().save(*args, **kwargs)

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    check_in = models.DateTimeField(null=True, blank=True)
    check_out = models.DateTimeField(null=True, blank=True)
    date = models.DateField(default=timezone.now())

    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name} - {self.date}"

    
class Payroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    bonus = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    net_pay = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    date_generated = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.net_pay = self.salary + self.bonus - self.deductions
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name} - {self.net_pay}"

