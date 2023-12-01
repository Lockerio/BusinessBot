from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from app.database.database import async_engine

from app.database.serializers.user_serializer import AsyncUserSerializer

from app.database.services.user_service import AsyncUserService


async_session = sessionmaker(bind=async_engine, class_=AsyncSession, expire_on_commit=False)()

userSerializer = AsyncUserSerializer(async_session)

userService = AsyncUserService(userSerializer)
