from django.http import HttpResponse

def doctor_view(request):
    print("This is Doctor")
    return HttpResponse("This is Doctor")
