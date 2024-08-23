from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_async_engine("sqlite+aiosqlite:////var/data/storage.db")

AsyncSessionLocal = async_sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine)

Base = declarative_base()

async def configure():
    metadata = Base.metadata
    async with engine.begin() as connection:
        await connection.run_sync(metadata.create_all)
