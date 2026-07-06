from django.http import HttpResponse

def employee_view(request):
    print("This is Employee")
    return HttpResponse("This is Employee")
