users_table_query="""
CREATE TABLE IF NOT EXISTS users(
id TEXT PRIMARY KEY,
first_name TEXT,
last_name TEXT,
email TEXT UNIQUE,
password TEXT,
phone    VARCHAR(20),
isAdmin  BOOLEAN,
created_at TEXT,
updated_at TEXT
)"""


products_table_query="""
CREATE TABLE IF NOT EXISTS products(
id  TEXT PRIMARY KEY ,
name TEXT,
descri TEXT,
sku  TEXT UNIQUE,
category TEXT,
brand TEXT,
price REAL,
stock INTEGER,
image_url TEXT,
is_active BOOLEAN,
created_at TEXT,
updated_at TEXT)"""


carts_table_query="""
CREATE TABLE IF NOT EXISTS carts(
id TEXT PRIMARY KEY,
user_id TEXT,
created_at TEXT,
updated_at TEXT)"""


cart_items_table_query="""
CREATE TABLE IF NOT EXISTS cart_items(
id TEXT PRIMARY KEY,
cart_id TEXT,
product_id TEXT,
quantity INTEGER,
unit_price REAL)"""


orders_table_query="""
CREATE TABLE IF NOT EXISTS orders(
id TEXT PRIMARY KEY,
user_id TEXT,
status  TEXT,
total_amount REAL,
shipping_address TEXT,
payment_method	TEXT,
created_at	TEXT,
updated_at  TEXT)"""

order_items_table_query="""
CREATE TABLE IF NOT EXISTS order_items(
id TEXT PRIMARY KEY,
order_id TEXT,
product_id TEXT,
quantity	Integer,
unit_price	REAL,
subtotal    REAL)"""
#Cart Complete