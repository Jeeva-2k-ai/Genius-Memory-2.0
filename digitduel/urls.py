from django.urls import path
from . import views

app_name = 'digitduel'

urlpatterns = [
    path('instructions4/', views.ins4, name='instructions4'),
    path('countdown4/', views.count4, name='countdown4'),
    path('game4/', views.game4, name='game4'),
]
