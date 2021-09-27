from django.shortcuts import render
import requests
from django import forms
from countries.utils import COUNTRY_CHOICES

class CountryForm(forms.Form):
    country= forms.CharField(label='', widget=forms.Select(choices=COUNTRY_CHOICES, attrs= {
        'class': 'country_select'
    }))


def get_country(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            api_url = f"https://restcountries.com/v3/alpha/{form.cleaned_data.get('country')}"
            response = requests.get(api_url)
            x = response.json()
            currency_key = list(x[0]['currencies'])[0]
            languages_key = list(x[0]['languages'])[0]
            flag = x[0]['flags'][1]   
            form = CountryForm()
            name = x[0]['name']['common']
            form.country = name
            return render(request, 'home/home.html', {
                'name': name,
                'capital': x[0]['capital'][0],
                'subregion': x[0]['subregion'],
                'flag': flag,
                'area': x[0]['area'],
                'domain': x[0]['tld'][0],
                'coin': x[0]['currencies'][currency_key]['name'],
                'calling_code': x[0]['idd']['root'],
                'region': x[0]['region'],
                'subregion': x[0]['subregion'],
                'languages': x[0]['languages'][languages_key],
                'latitud': x[0]['latlng'][0],
                'longitud': x[0]['latlng'][1],
                'demonyms': x[0]['demonyms']['eng']['m'],
                'country_form': CountryForm(),
            })
    return render(request, 'home/home.html', {
        'country_form': CountryForm()
    })