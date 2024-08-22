from pydantic import BaseModel


class LongUrl(BaseModel):
    long_url: str
