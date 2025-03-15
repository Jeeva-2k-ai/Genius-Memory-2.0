from django.urls import path
from . import views

app_name = 'trivialab'

urlpatterns = [
    path('instructions2/', views.ins2, name='instructions2'),
    path('countdown2/', views.count2, name='countdown2'),
    path('game2/', views.game2, name='game2'),
]
