from django.shortcuts import render
import requests

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=c564add204759c12777125351876efbf'
    city = 'New York'
    response = requests.get(url.format(city)).json()

    city_weather = {
        'city': city,
        'temperature': response['main']['temp'],
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
    }

    context = {'city_weather': city_weather}
    return render(request, 'weather.html', context)
