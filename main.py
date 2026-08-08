from fastapi import FastAPI
from database.create_schema import create_schema
from handlers.auth import router as auth_router
from handlers.products import router as products_router


app=FastAPI()
create_schema()
app.include_router(auth_router)
app.include_router(products_router)
