from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    # Render the home.html template
    return render(request, 'generator/home.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        # Include uppercase characters if requested
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        # Include special characters if requested
        characters.extend(list('!@#$%&*()'))

    if request.GET.get('numbers'):
        # Include numbers if requested
        characters.extend(list('1234567890'))
    
    length = int(request.GET.get('length', 12))

    thePassword = ''
    for x in range(length):
        # Randomly select characters from the available options
        thePassword += random.choice(characters)
    
    # Render the password.html template with the generated password
    return render(request, 'generator/password.html', {'password': thePassword })

def about(request):
    # Render the about.html template
    return render(request, 'generator/about.html')