from django.http import HttpResponse

def teachers_view(request):
    print("Teacher Information")
    return HttpResponse("Teacher Information")
