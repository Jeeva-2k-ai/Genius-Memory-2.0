from django.urls import path
from . import views

app_name = 'bytebusters'

urlpatterns = [
    path('instructions5/', views.ins5, name='instructions5'),
    path('countdown5/', views.count5, name='countdown5'),
    path('game5/', views.game5, name='game5'),
]
