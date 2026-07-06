from django.http import HttpResponse

def members_view(request):
    print("Member Information")
    return HttpResponse("Member Information")
