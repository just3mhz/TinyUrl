from fastapi import APIRouter
from fastapi import HTTPException

from application.api.models import LongUrl
from application.storage import storage
from application.storage import TokenNotFoundError

router = APIRouter()


@router.post('/api/v1/short_urls', status_code=201)
async def store(payload: LongUrl):
    token = await storage.store(url=payload.long_url)
    return {"token": token}


@router.get('/api/v1/short_urls/{token}')
async def retrieve(token: str):
    try:
        url = await storage.retrieve(token=token)
        return {"url": url}
    except TokenNotFoundError:
        raise HTTPException(status_code=404)
