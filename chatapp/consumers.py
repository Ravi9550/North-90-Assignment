import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from django.utils import timezone
from asgiref.sync import sync_to_async
from .models import Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.me = self.scope["user"]
        self.other_username = self.scope["url_route"]["kwargs"]["username"]
        user_list = sorted([self.me.username, self.other_username])
        self.room_group_name = f"chat_{user_list[0]}_{user_list[1]}"
        print(f">>>> connect() called. me={self.me}, other={self.other_username}")
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        print(f">>>> disconnect() called. me={self.me}, other={self.other_username}")
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message_text = data["message"].strip()

        if not message_text:
            return

        other_user = await sync_to_async(User.objects.get)(username=self.other_username)

        await sync_to_async(Message.objects.create)(
            sender=self.me,
            receiver=other_user,
            content=message_text,
            timestamp=timezone.now()
        )

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message_text,
                "sender": self.me.username
            }
        )

    async def chat_message(self, event):
        message = event["message"]
        sender = event["sender"]
        await self.send(text_data=json.dumps({
            "message": message,
            "sender": sender
        }))
