from django.shortcuts import render

# Forms
from . forms import CityForm


# requests
from . requests import current_weather


# Create your views here.



def home(request):
    
    api_response = {}
    
    
    if request.method == 'POST':
        city_input = CityForm(request.POST) # from /forms.py
        
        if city_input.is_valid():
            city_name = city_input.cleaned_data['city_input'].lower().split()
            api_response = current_weather(request, city_name=city_name) # STORE API response
            
            print(api_response)
            print(city_name)   
            
            
            
            if 'error' in api_response:
                error_message = api_response['error']['message']
                api_response = {'error': f"Error fetching data: {error_message}"}
    
    else:
        city_input = CityForm()          
    
    
    context = {
        'city_input': city_input,
        'response': api_response
    }
    
    return render(request, 'weather/base.html', context=context )