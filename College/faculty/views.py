from django.http import HttpResponse

def faculty_view(request):
    print("this is fculty")
    return HttpResponse("this is faculty")
