import json
from asyncio import sleep
from random import randint

from channels.generic.websocket import AsyncWebsocketConsumer

from digits_app.utils import generate_json_digits


class WSConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await super().connect()

        while True:
            random_number = randint(1, 1000)
            await self.send(json.dumps({'message': random_number}))
            await sleep(1)
