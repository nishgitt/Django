from django.http import HttpResponse

def students_view(request):
    print("Student Information")
    return HttpResponse("Student Information")
