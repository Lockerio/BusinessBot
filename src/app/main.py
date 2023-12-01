from pyrogram import Client

from app.config import API_ID, API_HASH


application = Client('account', API_ID, API_HASH)


@application.on_message()
async def message_handler(client, message):
    await message.forward("me")


application.run()
