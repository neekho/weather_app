from django.http import HttpResponse
from django.shortcuts import render

import requests


# Create your views here.


def current_weather(request, city_name='Makati'):
    
    payload = {
        'key': 'c2fcd24120be45aabc3143744232608',
        'q': city_name,
    }
    response = requests.get('http://api.weatherapi.com/v1/current.json', params=payload)
    
    print(response.status_code)
    print(response.url)
    
    
    return response.json()

def home(request):
    
    api_response = {}
    api_response = current_weather(request, city_name='Tokyo')
    
    context = {
        
        
        'response': api_response
    }
    
    return render(request, 'weather/base.html', context=context )