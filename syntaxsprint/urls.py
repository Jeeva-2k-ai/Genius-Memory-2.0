from django.urls import path
from . import views

app_name = 'syntaxsprint'

urlpatterns = [
    path('instructions1/', views.ins1, name='instructions1'),
    path('countdown1/', views.count1, name='countdown1'),
    path('game1/', views.game1, name='game1'),
]
