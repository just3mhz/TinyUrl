import logging

from fastapi import FastAPI

from application.api.v1 import routes
from application.database import database

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.configure()


@app.on_event("shutdown")
async def shutdown():
    pass


app.include_router(routes.router)

logging.basicConfig(level=logging.INFO)