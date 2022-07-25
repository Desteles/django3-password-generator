from django.shortcuts import render
from django.http import HttpResponse
import random
import string

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    low_letters = list(string.ascii_lowercase)
    
    if request.GET.get('uppercase'):
        low_letters.extend(list(string.ascii_uppercase))
    if request.GET.get('numbers'):
        low_letters.extend(list('0123456789'))
    if request.GET.get('special'):
        low_letters.extend(list('!@#$%^&*()'))
        
    length = int(request.GET.get('length', 12))
    
    thepassword = ''
    for i in range(length):
        thepassword += random.choice(low_letters)
    return render(request, 'generator/password.html', {'password': thepassword})

def about_us(request):
    return render(request, 'generator/about.html')