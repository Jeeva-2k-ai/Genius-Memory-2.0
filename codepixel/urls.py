from django.urls import path
from . import views

app_name = 'codepixel'

urlpatterns = [
    path('instructions6/', views.ins6, name='instructions6'),
    path('countdown6/', views.count6, name='countdown6'),
    path('game6/', views.game6, name='game6'),
]
