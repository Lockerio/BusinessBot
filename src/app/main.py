import asyncio
from datetime import timedelta

from pyrogram import Client
from sqlalchemy import func

from app.config import API_ID, API_HASH, FAVORITES_CHAT_ID
from app.database.container import userService, delayedMessageService, messageTemplateService


application = Client('account', API_ID, API_HASH)


async def periodic_check():
    while True:
        await asyncio.sleep(10)
        messages_to_send = await delayedMessageService.get_all_by_elapsed_time()

        if messages_to_send:
            print(messages_to_send)
            for message in messages_to_send:
                message_title = message.title
                user_id = message.user_id

                await application.send_message(message.chat_id, message.template.text)

                delayedMessageService.delete(message)
                message_template = None

                match message_title:
                    case 'first_message':
                        message_template = await messageTemplateService.get_one(2)
                        break

                    case 'second_message':
                        message_template = await messageTemplateService.get_one(4)
                        break

                if message_template:
                    current_time = func.now()
                    time_to_send_delta = timedelta(minutes=message_template['delay_time'])
                    delayed_time = current_time + time_to_send_delta

                    delayedMessageService.create({
                        'user_id': user_id,
                        'message_id': message_template.id,
                        'time_to_send': delayed_time
                    })

        print("Цикл проверки прошел!")
        await asyncio.sleep(10)


@application.on_message()
async def message_handler(client, message):
    tg_user = message.from_user
    chat_id = message.chat.id

    if message.text == '/users_today' and chat_id == FAVORITES_CHAT_ID:
        n = len(await userService.get_all_today())
        await application.send_message(chat_id, f'{n}')

    if tg_user:
        user = await userService.get_one(tg_user.id)
        if user:
            pass
        else:
            user_data = {
                'id': tg_user.id,
                'registration_date': func.current_date(),
                'chat_id': chat_id,
                'first_name': tg_user.first_name,
                'last_name': tg_user.last_name,
                'username': tg_user.username,
                'is_bot': tg_user.is_bot
            }
            await userService.create(user_data)

            current_time = func.now()
            message_template = await messageTemplateService.get_one(1)
            time_to_send_delta = timedelta(minutes=message_template.delay_time)
            delayed_time = current_time + time_to_send_delta

            await delayedMessageService.create({
                'user_id': tg_user.id,
                'message_id': message_template.id,
                'time_to_send': delayed_time
            })


async def main():
    async with application:
        await periodic_check()




if __name__ == '__main__':
    application.run(main())
