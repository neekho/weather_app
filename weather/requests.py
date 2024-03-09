import requests

from django.conf import settings


# Replace with your own API key
API_KEY = settings.API_KEY

def current_weather(request, city_name='Makati'):
    
    payload = {
        'key': API_KEY,
        'q': city_name,
    }
    response = requests.get('http://api.weatherapi.com/v1/current.json', params=payload)
    
    print(response.status_code)
    print(response.url)
    
    
    return response.json()