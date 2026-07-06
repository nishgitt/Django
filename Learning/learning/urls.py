from django.contrib import admin
from django.urls import path
from Courses.views import courses_view
from Students.views import students_view
from Trainers.views import trainers_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', courses_view, name='courses'),
    path('courses', courses_view),
    path('students/', students_view, name='students'),
    path('students', students_view),
    path('trainers/', trainers_view, name='trainers'),
    path('trainers', trainers_view),
]
