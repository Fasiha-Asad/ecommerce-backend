from fastapi import FastAPI
app=FastAPI()
from Database.create_schema import create_schema
create_schema()