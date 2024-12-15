import json
from asyncio import sleep
from random import randint

from channels.generic.websocket import AsyncWebsocketConsumer

from digits_app.utils import generate_json_digit


class WSConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await super().connect()

        while True:
            await self.send(generate_json_digit())
            await sleep(1)
