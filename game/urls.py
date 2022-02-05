from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('play/<room_code>', views.game, name='game'),
]
