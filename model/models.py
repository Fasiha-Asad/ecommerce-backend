from pydantic import BaseModel

# -------------- Auth Model --------------

# Register model
class UserRegister(BaseModel):
    first_name : str
    last_name : str
    email : str
    password : str


#  Login Model 
class UserLogin(BaseModel):
    email : str
    password : str

class UserUpdate(BaseModel):
    first_name: str
    last_name: str
    phone: str