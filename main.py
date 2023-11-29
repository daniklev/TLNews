
from telegramClient import TelethonClient
import asyncio
from datetime import timezone, datetime

async def main():
    api_id = 20819262
    api_hash = '90e1735c75461dddf93cf11ca53be47d'
    client = TelethonClient(api_id, api_hash)
    await client.start()

    # Display channels
    await client.display_user_channels()

    from_date = datetime(2023, 11, 28, tzinfo=timezone.utc)  # Example start date, timezone-aware
    to_date = datetime(2023, 11, 29, tzinfo=timezone.utc)# Example end date
    await client.get_messages_from_channel("N12 צ'אט הכתבים", from_date, to_date)

if __name__ == '__main__':
    asyncio.run(main())