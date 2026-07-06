from django.http import HttpResponse, JsonResponse

def home(request):
    return HttpResponse("Welcome to the Hospital App! Use /&lt;id&gt;/ (e.g., /123/) or /&lt;name&gt;/ (e.g., /john/) to see doctor details.")

def doc_id(request, id):
    return HttpResponse(f"Doctor ID: {id}")

def doc_name(request, name):
    return HttpResponse(f"Doctor Name: {name}")

def doctor_api(request):
    data = {
        "doctor_id": "D101",
        "doctor_name": "Dr. Ramesh Kumar",
        "specialization": "Cardiologist",
        "experience": "12 Years",
        "hospital": "City Hospital"
    }
    return JsonResponse(data)
