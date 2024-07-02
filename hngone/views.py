from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def hello(request):
    visitor_name = request.GET.get('visitor_name', 'Guest')
    client_ip = request.META.get('REMOTE_ADDR')
    location = "New York"  # Placeholder for actual location data
    temperature = "11"  # Placeholder for actual temperature data

    response_data = {
        "client_ip": client_ip,
        "location": location,
        "greeting": f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {location}"
    }

    return JsonResponse(response_data)