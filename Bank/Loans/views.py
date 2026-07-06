from django.http import HttpResponse

def loans_view(request):
    print("Loan Details")
    return HttpResponse("Loan Details")
