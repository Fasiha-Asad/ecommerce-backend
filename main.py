from fastapi import FastAPI
from database.create_schema import create_schema
from handlers.auth import router


app=FastAPI()
create_schema()
app.include_router(router)
