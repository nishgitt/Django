from django.http import HttpResponse

def transactions_view(request):
    print("Transaction History")
    return HttpResponse("Transaction History")
