from django.shortcuts import render
import datetime
from django.http import HttpResponse
import random

# Create your views here.
def hello(request):
    date = (datetime.datetime.now)
    return render(request, 'generator/home.html', {'date':date})

def password(request):
    pss =''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('number'):
        characters.extend('1234567890')
    if request.GET.get('special'):
        characters.extend('!@#$%^&*()?<>~')
    length = int(request.GET.get('length',10))
    if length >=6 and length <=25:
        for _ in range(length):
            pss +=  random.choice(characters)
    else:
        pass
    return render(request, 'generator/password.html', {'password':pss})


def about(request):
    return render(request, 'generator/about.html')