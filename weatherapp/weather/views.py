from django.shortcuts import render
import requests


def index(request):
    appid = 'dc7a59a4550ae730509e0659efcf4aa7'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid
    city = 'London'
    my_city = 'Gomel'
    res = requests.get(url.format(my_city))
    print(res.text)
    return render(request, 'weather/index.html')


def new(request):
    return render(request, 'weather/new.html')
