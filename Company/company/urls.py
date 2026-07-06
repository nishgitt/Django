from django.contrib import admin
from django.urls import path
from Employee.views import employee_view
from Department.views import department_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/', employee_view, name='employee'),
    path('employee', employee_view),
    path('department/', department_view, name='department'),
    path('department', department_view),
]
