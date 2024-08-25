import random
import typing
import logging

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import UrlRecord


class DatabaseRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, url: str, salt_range: typing.Tuple[int, int]) -> UrlRecord:
        obj = await self._find_by_url(url=url)

        if obj is not None:
            return obj
        
        salt = random.randint(salt_range[0], salt_range[1] - 1)
        obj = UrlRecord(salt, url)

        self.session.add(obj)
        await self.session.commit()
        await self.session.refresh(obj)
        return obj

    async def get(self, id: int) -> (UrlRecord | None):
        return await self.session.get(UrlRecord, id)

    async def _find_by_url(self, url: str) -> (UrlRecord | None):
        statement = select(UrlRecord).where(UrlRecord.url == url)
        return await self.session.scalar(statement=statement)
