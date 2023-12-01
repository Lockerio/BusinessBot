from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from app.database.database import async_engine

from app.database.serializers.user_serializer import AsyncUserSerializer
from app.database.services.delayed_message_service import AsyncDelayedMessageService
from app.database.services.message_template_service import AsyncMessageTemplateService

from app.database.services.user_service import AsyncUserService
from app.database.serializers.delayed_message_serializer import AsyncDelayedMessageSerializer
from app.database.serializers.message_template_serializer import AsyncMessageTemplateSerializer


async_session = sessionmaker(bind=async_engine, class_=AsyncSession, expire_on_commit=False)()

userSerializer = AsyncUserSerializer(async_session)
messageTemplateSerializer = AsyncMessageTemplateSerializer(async_session)
delayedMessageSerializer = AsyncDelayedMessageSerializer(async_session)

userService = AsyncUserService(userSerializer)
messageTemplateService = AsyncMessageTemplateService(messageTemplateSerializer)
delayedMessageService = AsyncDelayedMessageService(delayedMessageSerializer)
