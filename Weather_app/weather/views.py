from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=68d23bc96f5f287698b3e30040550afb'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    weather_data = []

    cities = City.objects.all()

    for city in cities:

        response = requests.get(url.format(city)).json()
        print(response)
        city_weather = {
        'city': city.name,
        'temperature': response['main']['temp'],
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
        }
        weather_data.append(city_weather)
        

    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'weather.html', context)
