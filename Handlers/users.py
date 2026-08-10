from fastapi import APIRouter,Header
from database.connection import conn,cursor
from handlers.auth import verify_token
from model.models import UserUpdate
router=APIRouter()

@router.get("/users/me")
def get_current_user(authorization:str=Header()):
    token=authorization.replace("Bearer ","")
    payload=verify_token(token)
    user_id=payload["user_id"]

    cursor.execute("""
    SELECT id, first_name, last_name, email, phone, created_at, updated_at
    FROM users
    WHERE id=?
    """,(user_id,))
    user=cursor.fetchone()
    return user

@router.put("/users/me")
def upd_current_user(user:UserUpdate,authorization:str=Header()):
    token=authorization.replace("Bearer ","")
    payload=verify_token(token)
    user_id=payload["user_id"]

    cursor.execute("""
    UPDATE users 
    SET first_name=?,
        last_name=?,
        phone=?
    where id=?
    """,
    (
        user.first_name,
        user.last_name,
        user.phone,
        user_id
    ))
    conn.commit()
    return  {
        "messages":"User updated successfully"
    }

@router.delete("/users/me")
def del_current_user(authorization:str=Header()):
    token=authorization.replace("Bearer ","")
    payload=verify_token(token)
    user_id=payload["user_id"]
    
    cursor.execute("""
    DELETE FROM users 
    WHERE id=?
    """,
    (
        user_id
    ))
    conn.commit()
    return {
        "messages":"User deleted successfully"
    }


