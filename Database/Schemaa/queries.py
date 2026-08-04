users_table_query="""
CREATE TABLE users(
id INTEGER PRIMARY KEY ,
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
CREATE TABLE products(
id INTEGER PRIMARY KEY ,
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
CREATE TABLE carts(
id INTEGER PRIMARY KEY,
user_id INTEGER,
created_at TEXT,
updated_at TEXT)"""


cart_items_table_query="""
CREATE TABLE cart_items(
id INTEGER PRIMARY KEY,
cart_id INTEGER,
product_id INTEGER,
quantity INTEGER,
unit_price REAL)"""


order_table_query="""
CREATE TABLE order(
id INTEGER PRIMARY KEY,
user_id INTEGER,
status  TEXT,
total_amount REAL,
shipping_address TEXT,
payment_method	TEXT,
created_at	TEXT,
updated_at  TEXT)"""

order_items_table_query="""
CREATE TABLE order_items(
id	INTEGER PRIMARY KEY,
order_id	INTEGER,
product_id	INTEGER,
quantity	Integer,
unit_price	REAL,
subtotal    REAL)"""