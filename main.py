from fastapi import FastAPI
from database.create_schema import create_schema
from handlers.auth import router as auth_router
from handlers.products import router as products_router
from handlers.cart import router as cart_router
from handlers.orders import router as orders_router
from handlers.users import router as users_router


app=FastAPI()
create_schema()
app.include_router(auth_router)
app.include_router(products_router)
app.include_router(cart_router)
app.include_router(orders_router)
app.include_router(users_router
