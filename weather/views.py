import json
from django.shortcuts import render

# Forms
from . forms import CityForm


# requests
from . requests import current_weather, forecast_weather


# Create your views here.


def home(request):
    '''
        accept and handle user input using forms.py in this case we created CityForm
    	we make requests using the requests.py
        see base.html in the templates folder.

    '''
    
    api_response = {}
    forecast_response = {}

    
    if request.method == 'POST':
        city_input = CityForm(request.POST) # from /forms.py
        
        if city_input.is_valid():
            city_name = city_input.cleaned_data['city_input'].lower().split()
            api_response = current_weather(request, city_name=city_name) # STORE API response
            forecast_response = forecast_weather(request, city_name=city_name)

            print(json.dumps(forecast_response, indent=4))   
            
            
            
            if 'error' in api_response:
                # This handles if a user tries to input a non existing city or an invalid input.
                error_message = api_response['error']['message']
                api_response = {'error': f"Error fetching data: {error_message}"}
                forecast_response = {'error': f"Error fetching data: {error_message}"}
                print(api_response)
                print(forecast_response)
    
    else:
        city_input = CityForm()          
    
    
    context = {
        'city_input': city_input,
        'response': api_response,
        'forecast': forecast_response
    }
    
    return render(request, 'weather/base.html', context=context )