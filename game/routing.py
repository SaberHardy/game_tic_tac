from django.urls import re_path
from game.consumer import TicTakToe

websocket_urlpatterns = [
    re_path(r'ws/play/(?P<room_code>\w+)/$', TicTakToe.as_asgi())
]
