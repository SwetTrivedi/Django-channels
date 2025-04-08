from django.urls import path
from . import consumer

websocket_urlpatterns=[
    path('ws/sc/', consumer.Mysyncconsumer.as_asgi()),
    path('ws/ac/',consumer.MyAsyncconsumer.as_asgi()),
]