from app.models.users_model import User


async def start_negotiate(
        payload: User
):
    await payload.insert()

    return {
        "session_id": str(payload.id)
    }
