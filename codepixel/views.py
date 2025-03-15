from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import time

# View for the Instructions page
def ins6(request):
    return render(request, 'instruction6.html')

# View for the Countdown page
def count6(request):
    return render(request, 'countdown6.html')

# View for the Game page (where questions will appear)
def game6(request):
    # Example for generating a code challenge (you can modify this to be dynamic)
    return render(request, 'game_page6.html')

