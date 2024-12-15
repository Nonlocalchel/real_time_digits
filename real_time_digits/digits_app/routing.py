from django.urls import path

from digits_app.consumers import WSConsumer

ws_urlpatterns = [
    path('ws/some-url', WSConsumer.as_asgi())
]