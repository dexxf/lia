from sqlalchemy.ext.asyncio import async_sessionmaker

from tin.shared.persistence.database import engine

SessionFactory = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    autoflush=False,
)