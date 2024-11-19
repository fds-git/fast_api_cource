from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
import logging
import os 

logger = logging.getLogger(__name__)

DATABASE_URL = os.getenv('DATABASE_URL')
logger.info(DATABASE_URL)

engine = create_async_engine(DATABASE_URL)

async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# BASE - для миграции (аккумулируются данные о всех моделях, которые от BASE отнаследуются)
class Base(DeclarativeBase):
    pass