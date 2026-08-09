from fastapi import APIRouter
from database.connection import conn,cursor
from model.models import CartItemsCreate
router=APIRouter()
import uuid
@router.get("/cart")
def get_cart():
    cursor.execute("""
    SELECT * FROM carts
    """)
    cart = cursor.fetchall()
    return cart

@router.post("/cart/items")
def additemscart (items:CartItemsCreate):
    items_id=str(uuid.uuid4())
    cursor.execute("""
    SELECT id FROM carts
     """)
    cart=cursor.fetchone()
    cart_id=cart[0]
   
    cursor.execute("""
    SELECT price FROM products WHERE id =?
    """,
    (items.product_id,))
    product=cursor.fetchone()
    unit_price=product[0]

    cursor.execute("""
    INSERT INTO cart_items(
    id,
    cart_id,
    product_id,
    quantity,
    unit_price)
    VALUES(?,?,?,?,?)
    """ ,
    (
        items_id,
        cart_id,
        items.product_id,
        items.quantity,
        unit_price
    ))

     conn.commit()

    return {
        "message": "Add items successfully"

    }   