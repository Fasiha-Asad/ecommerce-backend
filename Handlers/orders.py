from fastapi import APIRouter
from database.connection import conn,cursor
from model.models import OrderCreate
router=APIRouter()