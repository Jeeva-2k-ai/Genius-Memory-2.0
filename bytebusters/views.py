from django.shortcuts import render
import random

# View for the Instructions page
def ins5(request):
    return render(request, 'instruction5.html')

# View for the Countdown page
def count5(request):
    return render(request, 'countdown5.html')

# View for the Game page (where questions will appear)
def game5(request):
    return render(request, 'game_page5.html')
