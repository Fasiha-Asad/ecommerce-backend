from fastapi import APIRouter,Header
from database.connection import conn,cursor
from handlers.auth import verify_token
router=APIRouter()

@router.get("/users/me")
def get_current_user(authorization:str=Header()):
    token=authorization.replace("Bearer","")
    payload=verify_token(token)
    user_id=payload["user_id"]

    cursor.execute("""
    SELECT id, first_name, last_name, email, phone, created_at, updated_at
    FROM users
    WHERE id=?
    """,(user_id))
    user=cursor.fetchone()
    return user

