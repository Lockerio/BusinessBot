from pyrogram import Client

from app.config import API_ID, API_HASH
from app.database.container import userService

application = Client('account', API_ID, API_HASH)


@application.on_message()
async def message_handler(client, message):
    tg_user = message.from_user
    chat_id = message.chat.id

    user = await userService.get_one(tg_user.id)
    if user:
        pass
    else:
        user_data = {
            'id': tg_user.id,
            'chat_id': chat_id,
            'first_name': tg_user.first_name,
            'last_name': tg_user.last_name,
            'username': tg_user.username,
            'is_bot': tg_user.is_bot
        }
        await userService.create(user_data)

    await application.send_message(chat_id, "Hello")


application.run()
