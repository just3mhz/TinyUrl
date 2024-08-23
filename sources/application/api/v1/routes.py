from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Depends

from application.database import repository
from application.lib.encoder import encode
from application.lib.encoder import decode

from .schemas import LongUrl
from .depencies import get_repository

router = APIRouter(prefix='/api/v1')


SALT_RANGE = (0, 1000)

@router.post('/short_urls', status_code=201)
async def store(payload: LongUrl, repository: repository.DatabaseRepository = Depends(get_repository)):
    url_record = await repository.create(url=payload.long_url, salt_range=SALT_RANGE)
    token = encode(url_record.id * SALT_RANGE[1] + url_record.salt)
    return {"token": token}


@router.get('/short_urls/{token}')
async def retrieve(token: str, repository: repository.DatabaseRepository = Depends(get_repository)):
    id = decode(token) // SALT_RANGE[1]
    url_record = await repository.get(id=id)

    if url_record is None:
        raise HTTPException(status_code=404)
    
    return {"url": url_record.url}
