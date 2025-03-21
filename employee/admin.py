from django.contrib import admin
from .models import Employee, LeaveRequest,Attendance

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'department', 'position', 'hire_date','leave_balance','attendance_status')
    search_fields = ('first_name', 'last_name', 'email')

@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ('employee', 'leave_type', 'start_date', 'end_date', 'status')
    list_filter = ('status', 'leave_type')
    search_fields = ('employee__first_name', 'employee__last_name')
    actions = ['approve_leave', 'reject_leave']

    def approve_leave(self, request, queryset):
        for leave in queryset:
            leave.status = 'Approved'
            leave.save()

    def reject_leave(self, request, queryset):
        queryset.update(status='Rejected')

    approve_leave.short_description = "Approve Selected Leave Requests"
    reject_leave.short_description = "Reject Selected Leave Requests"


from .models import Payroll

@admin.register(Payroll)
class PayrollAdmin(admin.ModelAdmin):
    list_display = ('employee', 'salary', 'bonus', 'deductions', 'net_pay', 'date_generated')

    from .models import Attendance

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'check_in', 'check_out', 'date')
    list_filter = ('employee', 'date')
