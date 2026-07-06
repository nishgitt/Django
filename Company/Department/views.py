from django.http import HttpResponse

def department_view(request):
    print("This is Department")
    return HttpResponse("This is Department")
