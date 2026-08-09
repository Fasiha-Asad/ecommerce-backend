from fastapi import APIRouter
from database.connection import conn, cursor
from model.models import ProductCreate
import uuid
router= APIRouter()
@router.get("/products")
def get_products():
    cursor.execute("""
    SELECT * FROM products
    """)          
    products=cursor.fetchall()

    return products   

@router.get("/products/{id}")
def get_product(id:str):
    cursor.execute("""
    SELECT * FROM products WHERE id=?
    """,(id,))          
    product=cursor.fetchone()
    return product 

@router.post("/products")
def create_product(product:ProductCreate):
    product_id=str(uuid.uuid4())
    cursor.execute("""
    INSERT into products(
        id,
        name,
        description,
        sku,
        category,
        brand,
        price,
        stock,
        image_url,
        is_active
        )
    VALUES(?,?,?,?,?,?,?,?,?,?)
    """,
    (
        product_id,
        product.name,
        product.description,
        product.sku,
        product.category,
        product.brand,
        product.price,
        product.stock,
        product.image_url,
        product.is_active
    ))
    conn.commit()

    return {
        "id":product_id,
        "message": "product created successfully"

    }    
