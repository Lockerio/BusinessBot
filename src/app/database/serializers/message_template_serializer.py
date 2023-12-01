from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import MessageTemplate


class AsyncMessageTemplateSerializer:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_one(self, message_template_id):
        async with self.session.begin():
            result = await self.session.execute(select(MessageTemplate).where(MessageTemplate.id == message_template_id))
            return await result.scalar()

    async def get_one_by_title(self, title):
        async with self.session.begin():
            result = await self.session.execute(
                select(MessageTemplate).where(MessageTemplate.title == title)
            )
            return await result.scalar()

    async def get_all(self):
        async with self.session.begin():
            result = await self.session.execute(select(MessageTemplate))
            return result.scalars().all()

    async def create(self, data):
        user = MessageTemplate(**data)
        async with self.session.begin():
            self.session.add(user)
        return user

    async def update(self, message_template):
        async with self.session.begin():
            self.session.add(message_template)
        return message_template

    async def delete(self, message_template_id):
        message_template = await self.get_one(message_template_id)
        async with self.session.begin():
            await self.session.delete(message_template)
