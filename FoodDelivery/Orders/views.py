from django.http import HttpResponse

def orders_view(request):
    print("Order Details")
    return HttpResponse("Order Details")
