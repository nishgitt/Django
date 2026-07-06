from django.http import HttpResponse

def trainers_view(request):
    print("Trainer Dashboard")
    return HttpResponse("Trainer Dashboard")
