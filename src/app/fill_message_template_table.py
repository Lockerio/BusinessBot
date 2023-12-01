import asyncio
from app.database.container import messageTemplateService


async def fill_db():
    await messageTemplateService.create({
        'id': 1,
        'title': 'first_message',
        'text': 'Добрый день!',
        'delay_time': 10
    })

    await messageTemplateService.create({
        'id': 2,
        'title': 'second_message',
        'text': 'Подготовила для вас материал',
        'delay_time': 90
    })

    await messageTemplateService.create({
        'id': 3,
        'title': 'photo',
        'text': 'https://profkompntz.ru/wp-content/uploads/2020/08/bFHmVHvqvVQ-875x1024.jpg',
        'delay_time': 0
    })

    await messageTemplateService.create({
        'id': 4,
        'title': 'third_message',
        'text': 'Скоро вернусь с новым материалом!',
        'delay_time': 120
    })

if __name__ == '__main__':
    asyncio.run(fill_db())
