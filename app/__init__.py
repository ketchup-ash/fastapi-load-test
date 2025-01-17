from contextlib import asynccontextmanager
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from app.config import Settings
from app.models.users_model import User
from app.routers import (
    websocket_route,
    negotiate_route
)

@asynccontextmanager
async def app_lifespan(app: FastAPI):
    client: AsyncIOMotorClient = AsyncIOMotorClient(
        Settings().COSMOS_CONNECTION_STRING,
        serverSelectionTimeoutMS=5000,
        connectTimeoutMS=10000,
        socketTimeoutMS=10000,
        retryWrites=True,
        maxPoolSize=50
    )

    await init_beanie(client["user-session"], document_models=[User])

    yield

    client.close()
    

app = FastAPI(lifespan=app_lifespan)

app.include_router(websocket_route.router)
app.include_router(negotiate_route.router)

@app.get("/")
def root():
    return {
        "status": "running."
    }
