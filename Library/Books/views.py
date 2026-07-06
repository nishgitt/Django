from django.http import HttpResponse

def books_view(request):
    print("Book Information")
    return HttpResponse("Book Information")
