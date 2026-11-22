from sqlalchemy.ext.asyncio import create_async_engine
from tin.shared.config.config import settings

engine = create_async_engine(settings.DATABASE_URL,pool_pre_ping=True)