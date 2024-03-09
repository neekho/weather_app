import requests

API_KEY = 'c2fcd24120be45aabc3143744232608'

def current_weather(request, city_name='Makati'):
    
    payload = {
        'key': API_KEY,
        'q': city_name,
    }
    response = requests.get('http://api.weatherapi.com/v1/current.json', params=payload)
    
    print(response.status_code)
    print(response.url)
    
    
    return response.json()