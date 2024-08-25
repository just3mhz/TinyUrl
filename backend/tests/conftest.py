import pytest
import pytest_asyncio

from starlette.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from application.main import app
from application.database import database
from application.database import session
from application.database import models

@pytest_asyncio.fixture(scope='module')
async def get_db_session():
    engine = create_async_engine('sqlite+aiosqlite:///:memory:')
    
    async with engine.begin() as connection:
        await connection.run_sync(database.Base.metadata.drop_all)
        await connection.run_sync(database.Base.metadata.create_all)
    
    session = async_sessionmaker(engine)()

    session.add_all([
        models.UrlRecord(salt=0, url='https://www.some-url.com/1'),
        models.UrlRecord(salt=0, url='https://www.some-url.com/2'),
        models.UrlRecord(salt=0, url='https://www.some-url.com/3')
    ])
    await session.commit()

    yield session
    await session.close()

@pytest.fixture(scope='module')
def test_app(get_db_session):
    app.dependency_overrides[session.get_db_session] = lambda: get_db_session
    client = TestClient(app)
    yield client
