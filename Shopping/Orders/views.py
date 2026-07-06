from django.http import HttpResponse

def orders_view(request):
    print("Welcome to Orders")
    return HttpResponse("Welcome to Orders")
