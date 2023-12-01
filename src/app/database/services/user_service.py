from app.database.serializers.user_serializer import AsyncUserSerializer


class AsyncUserService:
    def __init__(self, serializer: AsyncUserSerializer):
        self.serializer = serializer

    async def get_one(self, user_id):
        return await self.serializer.get_one(user_id)

    async def get_all(self):
        return await self.serializer.get_all()

    async def create(self, data):
        if await self.get_one(data['id']):
            return False
        await self.serializer.create(data)
        return True

    async def update(self, data):
        user_id = data.get("id")
        try:
            user = await self.get_one(user_id)
            user.id = data.get("title")
            user.last_name = data.get("text")
            user.first_name = data.get("text")
            user.username = data.get("text")
            user.is_bot = data.get("url")
        except Exception:
            raise Exception('There is no such user in db.')

        return await self.serializer.update(user)

    async def delete(self, user_id):
        await self.serializer.delete(user_id)
