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

class ProductCreate(BaseModel):
    name: str
    description: str
    sku: str
    category: str
    brand: str
    price: float
    stock: int
    image_url: str
    is_active: bool


class ProductUpdate(BaseModel):
    name: str
    description: str
    sku: str
    category: str
    brand: str
    price: float
    stock: int
    image_url: str
    is_active: bool

class CartItemsCreate(BaseModel):
    product_id:str
    quantity:int

class CartItemUpdate(BaseModel):
    quantity: int

class OrderCreate(BaseModel):
    shipping_address: str
    payment_method: str
