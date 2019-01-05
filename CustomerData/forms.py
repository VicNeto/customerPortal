#Customer forms

#Django
from django import forms

class UserForm(forms.Form):
    #Create customer form

    first_name = forms.CharField(min_length=1,max_length=50)
    last_name = forms.CharField(min_length=1,max_length=50)

    address = forms.CharField(min_length=2,max_length=80)
    city = forms.CharField(min_length=2,max_length=80)
    state = forms.CharField(min_length=2,max_length=20)
    zip_number = forms.CharField(min_length=2,max_length=10)
