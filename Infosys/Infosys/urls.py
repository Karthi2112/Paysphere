from django.urls import path # type: ignore
from apis import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('logout/', views.user_logout, name='user_logout'),  
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),

    path('add_employee/', views.add_employee, name='add_employee'),
    path('employee_list/', views.employee_list, name='employee_list'),
    path('employee_detail/<int:employee_id>/', views.employee_detail, name='employee_detail'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('edit_employee/<int:employee_id>/', views.employee_edit, name='employee_edit'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('delete_employee/<int:employee_id>/', views.delete_employee, name='delete_employee'),

    
    path('approve-leave-request/<int:leave_request_id>/', views.approve_leave_request, name='approve_leave_request'),
    path('reject-leave-request/<int:leave_request_id>/', views.reject_leave_request, name='reject_leave_request'),
    path('leave-request/update/<int:leave_request_id>/', views.update_leave_request, name='update_leave_request'),
    path('leave-request/delete/<int:leave_request_id>/', views.delete_leave_request, name='delete_leave_request'),
    path('leave-requests/', views.leave_requests, name='leave_requests'),
    path('leave_list/', views.leave_list, name='leave_list'),
    path('review_leave_request/<int:leave_request_id>/', views.review_leave_requests, name='review_leave_requests'),
    path('create_leave_request/', views.create_leave_request, name='create_leave_request'),
    path('generate_payroll/', views.generate_payroll, name='generate_payroll'),



    path('', views.home, name='home'),
]
