from django.http import HttpResponse

def students_view(request):
    print("Student Dashboard")
    return HttpResponse("Student Dashboard")
