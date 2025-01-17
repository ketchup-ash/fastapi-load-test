from contextlib import asynccontextmanager
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from app.config import Settings
from app.routers import websocket_route

@asynccontextmanager
async def app_lifespan(app: FastAPI):
    client: AsyncIOMotorClient = AsyncIOMotorClient(
        Settings().COSMOS_CONNECTION_STRING
    )

    yield
    

app = FastAPI(lifespan=app_lifespan)

app.include_router(websocket_route.router)

@app.get("/")
def root():
    return {
        "status": "running."
    }
