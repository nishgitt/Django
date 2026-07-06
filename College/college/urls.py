from django.contrib import admin
from django.urls import path

# Capitalize the 'S' and 'F' to match your actual folder names
from student.views import student_view
from faculty.views import faculty_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', student_view, name='student'),
    path('faculty/', faculty_view, name='faculty'),
]