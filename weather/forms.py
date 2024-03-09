from django import forms

# In Django, forms are a crucial part of the framework's built-in tools for handling user input. 
# Forms are used to define the fields and behavior of HTML forms, making it easier to 
# handle data validation, display, and submission. 
# Django forms simplify the process of collecting and processing user input by providing a high-level abstraction.




class CityForm(forms.Form):
    city_input = forms.CharField(label='city name...')
    
    

# class CityForm(forms.Form): 
# This line defines a new class named CityForm that inherits from forms.Form. This means that CityForm is a subclass of Django's generic Form class.

# city_input = forms.CharField(label='city name...') 
# This line defines a form field named city_input within the CityForm class. It is an instance of the CharField class, 
# which represents a single-line text input. The label parameter sets the label that will be displayed next to the input field in the form.