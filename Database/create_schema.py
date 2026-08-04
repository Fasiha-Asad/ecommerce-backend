from connection import conn, cursor

from Schema.queries import (
    users_table_query,
    products_table_query,
    carts_table_query,
    cart_items_table_query,
    orders_table_query,
    order_items_table_query
)
def create_schema():

    cursor.execute(users_table_query)
    cursor.execute(products_table_query)
    cursor.execute(carts_table_query)
    cursor.execute(cart_items_table_query)
    cursor.execute(orders_table_query)
    cursor.execute(order_items_table_query)
    conn.commit()