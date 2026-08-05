import sqlite3
conn = sqlite3.connect("ecommerce.db",check_same_thread=False)
conn.row_factory=sqlite3.Row
cursor=conn.cursor()