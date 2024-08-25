from pydantic import BaseModel


class UrlPayload(BaseModel):
    url: str


class TokenPayload(BaseModel):
    token: str
