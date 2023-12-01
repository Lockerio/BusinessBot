from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import DelayedMessage


class AsyncDelayedMessageSerializer:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_one(self, delayed_message_id):
        async with self.session.begin():
            result = await self.session.execute(select(DelayedMessage).where(DelayedMessage.id == delayed_message_id))
            return await result.scalar()

    async def get_all(self):
        async with self.session.begin():
            result = await self.session.execute(select(DelayedMessage))
            return result.scalars().all()

    async def create(self, data):
        user = DelayedMessage(**data)
        async with self.session.begin():
            self.session.add(user)
        return user

    async def update(self, delayed_message):
        async with self.session.begin():
            self.session.add(delayed_message)
        return delayed_message

    async def delete(self, delayed_message_id):
        delayed_message = await self.get_one(delayed_message_id)
        async with self.session.begin():
            await self.session.delete(delayed_message)
