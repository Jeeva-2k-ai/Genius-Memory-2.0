from django.urls import path
from . import views

app_name = 'codebreakers'

urlpatterns = [
    path('instructions3/', views.ins3, name='instructions3'),
    path('countdown3/', views.count3, name='countdown3'),
    path('game3/', views.game3, name='game3'),
]
