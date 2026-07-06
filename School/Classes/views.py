from django.http import HttpResponse

def classes_view(request):
    print("Class Information")
    return HttpResponse("Class Information")
