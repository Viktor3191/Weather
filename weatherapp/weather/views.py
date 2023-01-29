from django.shortcuts import render

def index(request):
    return render(request, 'weather/index.html')


def new(request):
    return render(request, 'weather/new.html')
