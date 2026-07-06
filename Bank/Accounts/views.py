from django.http import HttpResponse

def accounts_view(request):
    print("Account Details")
    return HttpResponse("Account Details")
