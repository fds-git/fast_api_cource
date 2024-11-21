from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
import logging
import os 
from app.config import settings

logger = logging.getLogger(__name__)

logger.info(settings.DATABASE_URL)
engine = create_async_engine(settings.DATABASE_URL)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# BASE - для миграции (аккумулируются данные о всех моделях, которые от BASE отнаследуются)
class Base(DeclarativeBase):
    pass