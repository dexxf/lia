from collections.abc import AsyncIterator

from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession

from tin.shared.persistence.database import engine

SessionFactory = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    autoflush=False,
)

async def get_session() -> AsyncIterator[AsyncSession]:
    async with SessionFactory() as session:
        async with session.begin():
            yield session
