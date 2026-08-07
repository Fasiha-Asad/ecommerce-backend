from fastapi import APIRouter,HTTPException,Header
import uuid
from database.connection import conn, cursor
from model.models import UserRegister, UserLogin
from passlib.context import CryptContext
from jose import jwt,JWTError
from datetime import datetime,timedelta,timezone
# Router
router= APIRouter()

#password hashing
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)
#JWT
SECRET_KEY="my_secret_key"
ALGORITHM="HS256"

def verify_token(token:str):
    try:
        payload=jwt.decode(
           token,
           SECRET_KEY,
           algorithms=[ALGORITHM] #list for multiple algo
    )
        return payload
    except JWTError:
        raise HTTPException(
        status_code=401,
        detail="INVALID TOKEN"

        )

# To register users
@router.post("/register")
def register(user:UserRegister):
    user_id = str(uuid.uuid4())
    hashed_password=pwd_context.hash(user.password)
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
       hashed_password
    )
    )
    conn.commit()
    return{
        "email":user.email,
        "message":"User Registered"
    }


@router.post("/login")
def login(user:UserLogin):
    cursor.execute("""
    SELECT * FROM users WHERE email = ?
    """,
    (user.email,))
    user_data = cursor.fetchone()
    if user_data is None:
        return {
        "message": "User not found"
    }
    if not pwd_context.verify(user.password,user_data["password"]):
        return{
            "message":"Invalid Password"
        }
    expire=datetime.now(timezone.utc)+timedelta(minutes=30)

    payload={

            "user_id":user_data["id"],
            "exp": expire
            }
    token=jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    return {
        "email":user.email,
        "token": token,
        "message":"User Login"
    }
@router.get("/profile")
def profile(authorization:str= Header()):
    token=authorization.replace("Bearer ","")
    payload=verify_token(token)

    return {
        "user_id":payload["user_id"],
        "message":"Profile Access"

    }

