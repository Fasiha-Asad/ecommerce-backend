from fastapi import APIRouter
from database.connection import conn, cursor
router= APIRouter()
@router.get("/product")
def get_products():
    cursor.execute("""
    SELECT * FROM products
    """)          
    products=cursor.fetchall()

    return products   