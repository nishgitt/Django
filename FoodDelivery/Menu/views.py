from django.http import HttpResponse

def menu_view(request):
    print("Food Menu")
    return HttpResponse("Food Menu")
