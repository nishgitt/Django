from django.http import HttpResponse

def student_view(request):
    print("this is a student")
    return HttpResponse("this is a student")
