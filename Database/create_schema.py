def create_schema():

    cursor.execute(users_table_query)
    cursor.execute(products_table_query)
    cursor.execute(carts_table_query)
    cursor.execute(cart_items_table_query)
    cursor.execute(orders_table_query)
    cursor.execute(order_items_table_query)
    conn.commit()