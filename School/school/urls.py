from django.contrib import admin
from django.urls import path
from Students.views import students_view
from Teachers.views import teachers_view
from Classes.views import classes_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', students_view, name='students'),
    path('students', students_view),
    path('teachers/', teachers_view, name='teachers'),
    path('teachers', teachers_view),
    path('classes/', classes_view, name='classes'),
    path('classes', classes_view),
]
