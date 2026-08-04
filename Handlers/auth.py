from fastapi import APIRouter
from pydantic import BaseModel
import uuid
from Database.connection import conn, cursor
router= APIRouter()

class UserRegister(BaseModel):
    first_name : str
    last_name : str
    email : str
    password : str

@router.post("/register")
def register(user:UserRegister):
    user_id = str(uuid.uuid4())
    cursor.execute("""
    INSERT INTO users(
    id,
    first_name ,
    last_name,
    email,
    password
    )
    VALUES(?,?,?,?,?)
    """,
    (
        user_id,
        user.first_name,
        user.last_name,
        user. email,
        user.password
    )
    )
    conn.commit()
    return{
        "email":user.email,
        "message":"User Registered"
    }



