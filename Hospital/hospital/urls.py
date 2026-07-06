from django.contrib import admin
from django.urls import path
from Doctor.views import doctor_view
from Patient.views import patient_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('doctor/', doctor_view, name='doctor'),
    path('doctor', doctor_view),
    path('patient/', patient_view, name='patient'),
    path('patient', patient_view),
]
