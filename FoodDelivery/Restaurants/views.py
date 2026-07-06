from django.http import HttpResponse

def restaurants_view(request):
    print("Restaurant List")
    return HttpResponse("Restaurant List")
