from fastapi import APIRouter
from database.connection import conn,cursor
from model.models import CartItemsCreate
router=APIRouter()
@router.get("/cart")
def get_cart():
    cursor.execute("""
    SELECT * FROM carts
    """)
    cart = cursor.fetchall()
    return cart