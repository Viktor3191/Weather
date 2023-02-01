from django.shortcuts import render
import requests


def index(request):
    appid = 'dc7a59a4550ae730509e0659efcf4aa7'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid
    city = 'London'
    res = requests.get(url.format(city)).json()
    city_info = {
        'city': city,
        'temp': res['main']['temp'],
        'icon': res['weather'][0]['icon']
    }
    context = {'info': city_info}

    return render(request, 'weather/index.html', context)


def new(request):
    appid = 'dc7a59a4550ae730509e0659efcf4aa7'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid
    # city = 'New York'
    city = 'Gomel'
    res = requests.get(url.format(city)).json()
    city_info = {
        'city': city,
        'temp': res['main']['temp'],
        'icon': res['weather'][0]['icon'],
        'humidity': res['main']['humidity'],
        'speed': res['wind']['speed'],
        'all': res['clouds']['all'],
    }
    context = {'info': city_info}

    return render(request, 'weather/new.html', context)
