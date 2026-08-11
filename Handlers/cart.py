from fastapi import APIRouter, Depends
from fastapi.security import APIKeyHeader
from handlers.auth import verify_token
from database.connection import conn,cursor
from model.models import CartItemsCreate,CartItemUpdate
router=APIRouter()
import uuid
authorization_header = APIKeyHeader(
    name="Authorization"
)
@router.get("/cart")

def get_cart( authorization: str = Depends(authorization_header)):
   
    token = authorization.replace("Bearer ", "")
    payload = verify_token(token)
    user_id = payload["user_id"]
    cursor.execute("""
    SELECT * FROM carts
    WHERE user_id=?
    """, (user_id,))
    cart = cursor.fetchone()
    if cart is None:
        return []
    return cart


@router.post("/cart/items")
def additemscart(
    items: CartItemsCreate,
    authorization: str = Depends(authorization_header)):

    token = authorization.replace("Bearer ", "")
    payload = verify_token(token)
    user_id = payload["user_id"]
    items_id=str(uuid.uuid4())

    cursor.execute("""

    SELECT id FROM carts
    WHERE user_id=?
    """, (user_id,))

    cart = cursor.fetchone()

    if cart is None:

        cart_id = str(uuid.uuid4())

        cursor.execute("""
        INSERT INTO carts(id, user_id)
        VALUES(?, ?)
        """, (cart_id, user_id))

        conn.commit()

    else:

       cart_id = cart[0]

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
@router.put("/cart/items/{itemid}")
def upd_cart(itemid:str,upd_cart:CartItemUpdate):

    cursor.execute("""

    UPDATE cart_items
    SET
    quantity=?
    WHERE id=?
    """,
    (


       upd_cart.quantity,
       itemid
    ))

    conn.commit()

    return {
        "id": items_id,

        "message": "Cart item updated successfully"
    }
@router.delete("/cart/items/{itemid}")
def del_cart(itemid:str):

        cursor.execute("""


        DELETE from cart_items
        WHERE id=?
        """,(itemid,))

        conn.commit()

        return {

           "message": "Cart item deleted successfully"
        }
@router.delete("/cart")
def clear_cart():

    cursor.execute("""

    DELETE from cart_items
    """)
    conn.commit()

    return {
    "message": "Cart cleared successfully"
} 
    