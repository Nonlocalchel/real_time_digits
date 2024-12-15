from time import sleep

from channels.generic.websocket import WebsocketConsumer

from digits_app.utils import generate_json_digits


class WSConsumer(WebsocketConsumer):
    def connect(self):
        super().connect()

        while True:
            self.send(generate_json_digits())
            sleep(1)


