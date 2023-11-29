from telethon import TelegramClient, events, sync
import asyncio
from datetime import timezone, datetime

class TelethonClient:
    def __init__(self, session_name,api_id, api_hash):
        self.client = TelegramClient( session_name, api_id, api_hash)
        self.last_scan_date = {}

    async def start(self):
        await self.client.start()

    async def display_user_channels(self):
        async for dialog in self.client.iter_dialogs():
            if dialog.is_channel:
                print(dialog.name)

    async def search_user_channels(self, query):
        async for dialog in self.client.iter_dialogs():
            if dialog.is_channel and query.lower() in dialog.name.lower():
                print(dialog.name)

    async def get_messages_from_channel(self, channel, from_date=None, to_date=None):
        # Determine the time range for message retrieval
        if not from_date and not to_date:
            from_date = self.last_scan_date.get(channel, datetime.datetime.min.replace(tzinfo=timezone.utc))
            to_date = datetime.datetime.now().astimezone(timezone.utc)
        elif not to_date:
            to_date = datetime.datetime.now().astimezone(timezone.utc)
        else:
            to_date = to_date.astimezone(timezone.utc)

        from_date = from_date.astimezone(timezone.utc)

        channel_entity = await self.client.get_entity(channel)
        latest_message_date = None
        async for message in self.client.iter_messages(channel_entity, offset_date=to_date, reverse=True):
            if message.date < from_date:
                break
            print(message.sender_id, message.date, message.text)
            latest_message_date = message.date

        # Update the last scan date for the channel
        if latest_message_date:
            self.last_scan_date[channel] = latest_message_date