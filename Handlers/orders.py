from fastapi import APIRouter
from database.connection import conn,cursor
from model.models import OrderCreate
import uuid
from datetime import datetime
router=APIRouter()

@router.post("/orders")
def create_order(order:OrderCreate):

    cursor.execute("""
    SELECT id,user_id FROM carts
    """)
    cart=cursor.fetchone()
    cart_id=cart[0]
    user_id=cart[1]

    cursor.execute("""
    SELECT product_id,quantity,unit_price 
    FROM cart_items
    where cart_id=?
    """,(cart_id,))
    cart_items=cursor.fetchall()

    total_amount=0
    for item in cart_items:
        total_amount+=item[1]*item[2]
    
    order_id=str(uuid.uuid4())
    status="pending"
    created_at = datetime.now()
    updated_at = datetime.now()


    cursor.execute("""
    INSERT INTO orders(
    id ,
    user_id ,
    status  ,
    total_amount ,
    shipping_address ,
    payment_method	,
    created_at	,
    updated_at 
    VALUES(?,?,?,?,?,?,?,?)
    """,
    (
        order_id,
        user_id ,
        status  ,
        total_amount ,
        order.shipping_address ,
        order.payment_method	,
        created_at	,
        updated_at 
    ))
    for item in cart_items:
        order_item_id=str(uuid.uuid4())
        subtotal=item[1]*item[2]

        cursor.execute("""
        SELECT stock 
        FROM products 
        WHERE id=?
        """,(item[0],))
        product=cursor.fetchone()
        if product[0]<item[1]:#stock
            return {          #quantity
               "message": "Not enough stock"
               }

        cursor.execute("""
        INSERT INTO order_items(
        id ,
        order_id, 
        product_id, 
        quantity,	
        unit_price,	
        subtotal )
        VALUES(?,?,?,?,?,?) 
         """,
         (
            order_item_id,
            order_id,
            item[0],
            item[1],
            item[2],
            subtotal
         ))
        

        cursor.execute("""
        UPDATE products
        SET stock=stock-?
        WHERE id=?
        """,
        (

            item[1],
            item[0]
        ))

    conn.commit()
    return {
        "message":" Order created successfully"
    }
    
@router.get("/orders")
def get_order(user_id:str):
    cursor.execute("""
    SELECT *FROM orders
    WHERE user_id=?
    """,(user_id,))
    orders=cursor.fetchall()
    return orders
    
@router.get("/orders/{id}")
def get_order(id:str):
    cursor.execute("""
    SELECT *FROM orders
    WHERE id=?
    """,(id,))
    orders=cursor.fetchone()
    return orders

