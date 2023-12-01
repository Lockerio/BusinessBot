from app.database.serializers.delayed_message_serializer import AsyncDelayedMessageSerializer


class AsyncDelayedMessageService:
    def __init__(self, serializer: AsyncDelayedMessageSerializer):
        self.serializer = serializer

    async def get_one(self, delayed_message_id):
        return await self.serializer.get_one(delayed_message_id)

    async def get_all(self):
        return await self.serializer.get_all()

    async def create(self, data):
        if await self.get_one(data['id']):
            return False
        await self.serializer.create(data)
        return True

    async def delete(self, delayed_message_id):
        await self.serializer.delete(delayed_message_id)
