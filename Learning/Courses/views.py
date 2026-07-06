from django.http import HttpResponse

def courses_view(request):
    print("Available Courses")
    return HttpResponse("Available Courses")
