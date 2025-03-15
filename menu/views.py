from django.shortcuts import render

# Create your views here.

def game_menu(request):
    return render(request, 'game_menu.html')

