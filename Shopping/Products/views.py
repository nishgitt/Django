from django.http import HttpResponse

def products_view(request):
    print("Welcome to Products")
    return HttpResponse("Welcome to Products")
