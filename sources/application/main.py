import logging

from fastapi import FastAPI

from application.api import tinyurl
from application.storage import storage

app = FastAPI()

@app.on_event("startup")
async def startup():
    await storage.configure()


@app.on_event("shutdown")
async def shutdown():
    pass


app.include_router(tinyurl.router)

logging.basicConfig(level=logging.INFO)