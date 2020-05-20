from django.urls import path

from . import customers

websocket_urlpatterns=[
    path('ws/notes',consumers.NoteConsumer)
]
