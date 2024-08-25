from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .database import Base

class UrlRecord(Base):
    __tablename__ = 'storage'

    def __init__(self, salt, url):
        self.salt = salt
        self.url = url

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    salt: Mapped[int]
    url: Mapped[str] = mapped_column(String, unique=True)
