import asyncio
from fastapi import (
    APIRouter,
    WebSocket,
    WebSocketDisconnect,
    WebSocketException,
    status
)
from bson import ObjectId

from app.models.users_model import User

router = APIRouter(
    prefix="/ws",
    tags=["websocket"]
)

@router.websocket("/{session_id}")
async def chat_websocket(
        session_id: str,
        websocket: WebSocket,
):
    user = await User.find_one(User.id == ObjectId(session_id))
    await websocket.accept()

    try:
        while True:
            await websocket.receive_json()
            for i in [1,2,3,4,5,6,7,8,9,0]:
                await websocket.send_json({"data": str(i)})
                await asyncio.sleep(0.2)
            await websocket.send_json({"data": f"{user.name} and {user.age}"})
    except WebSocketDisconnect:
        pass
    except WebSocketException as e:
        await websocket.close(
            code=status.WS_1006_ABNORMAL_CLOSURE,
            reason=str(e)
        )
    finally:
        if user:
            await user.delete()

