from app.database.serializers.message_template_serializer import AsyncMessageTemplateSerializer


class AsyncMessageTemplateService:
    def __init__(self, serializer: AsyncMessageTemplateSerializer):
        self.serializer = serializer

    async def get_one(self, message_template_id):
        return await self.serializer.get_one(message_template_id)

    async def get_all(self):
        return await self.serializer.get_all()

    async def create(self, data):
        if await self.get_one(data['id']):
            return False
        await self.serializer.create(data)
        return True

    async def delete(self, message_template_id):
        await self.serializer.delete(message_template_id)
