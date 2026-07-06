from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def home(request):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Hospital Directory</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #f4f7f6;
                margin: 0;
                padding: 40px;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 80vh;
            }
            .container {
                background: white;
                padding: 40px;
                border-radius: 12px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.08);
                max-width: 500px;
                text-align: center;
            }
            h1 {
                color: #007bff;
                margin-bottom: 20px;
            }
            p {
                color: #555;
                font-size: 16px;
                line-height: 1.6;
            }
            .url-box {
                background: #f8f9fa;
                border-left: 4px solid #007bff;
                padding: 15px;
                margin: 20px 0;
                text-align: left;
                font-family: monospace;
                font-size: 14px;
            }
            .link-btn {
                display: inline-block;
                margin-top: 15px;
                padding: 10px 20px;
                background: #007bff;
                color: white;
                text-decoration: none;
                border-radius: 5px;
                font-weight: bold;
            }
            .link-btn:hover {
                background: #0056b3;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Hospital Directory</h1>
            <p>Welcome to the Hospital App! To search for doctor profiles, use one of the following URLs:</p>
            <div class="url-box">
                <!-- Links that point to doctor view and API view -->
                • Profile by ID: <a href="/101/">/101/</a><br>
                • Profile by Name: <a href="/ramesh/">/ramesh/</a><br>
                • JSON Doctor API: <a href="/doctor_api/">/doctor_api/</a>
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)

def doc_id(request, id):
    return render(request, 'doctor.html', {'id': id})

def doc_name(request, name):
    return render(request, 'doctor.html', {'name': name})

def doctor_api(request):
    data = {
        "doctor_id": "D101",
        "doctor_name": "Dr. Ramesh Kumar",
        "specialization": "Cardiologist",
        "experience": "12 Years",
        "hospital": "City Hospital"
    }
    return JsonResponse(data)
