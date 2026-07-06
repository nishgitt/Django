from django.http import HttpResponse

def patient_view(request):
    print("This is Patient")
    return HttpResponse("This is Patient")
