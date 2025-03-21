from django.urls import path
from .views import employee_list, employee_add, employee_edit, leave_request_list, leave_request_add,check_in,check_out,attendance_page,login_view,payroll

urlpatterns = [
    path('', employee_list, name='employee_list'),
    path('add/', employee_add, name='employee_add'),
    path('edit/<int:pk>/', employee_edit, name='employee_edit'),
    path('leave-requests/', leave_request_list, name='leave_request_list'),
    path('leave-requests/add/', leave_request_add, name='leave_request_add'),
    path('attendance/', attendance_page, name='attendance_page'),
    path('check-in/', check_in, name='check_in'),
    path('check-out/', check_out, name='check_out'),
    path('login/', login_view, name='login'),
    path('payroll/', payroll, name='payroll'),
]
