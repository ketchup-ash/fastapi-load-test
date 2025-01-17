from fastapi import (
    APIRouter,
    HTTPException,
    status
)
from fastapi.responses import JSONResponse

from app.controllers.negotiate_controller import start_negotiate
from app.models.users_model import User

router = APIRouter(
    prefix="/negotiate",
    tags=["negotiate"]
)

@router.post(
        path="/user",
        response_model=User
)
async def negotiate_user(
        payload: User,
):
    try:
        response = await start_negotiate(
            payload=payload
        )
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=response
        )
    except HTTPException as http_e:
        return JSONResponse(
            status_code=http_e.status_code,
            content=http_e.detail
        )
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "error": str(e)
            }
        )
