from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import time

# View for the Instructions page
def ins2(request):
    return render(request, 'instruction2.html')

# View for the Countdown page
def count2(request):
    return render(request, 'countdown2.html')

# View for the Game page (where questions will appear)
def game2(request):
    # Example for generating a code challenge (you can modify this to be dynamic)
    return render(request, 'game_page2.html')

