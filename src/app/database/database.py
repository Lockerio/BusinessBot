from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine

from app.config import DB_URL


async_engine = create_async_engine(DB_URL)
Base = declarative_base()
