from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.game_menu, name='menu'),
]
