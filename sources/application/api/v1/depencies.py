from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from application.database import session
from application.database import repository

def get_repository(session: AsyncSession = Depends(session.get_db_session)) -> repository.DatabaseRepository:
    return repository.DatabaseRepository(session=session)
