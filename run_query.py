import sqlite3
import pandas as pd

# Connect to the SQLite database
db_file = "ecom.db"
conn = sqlite3.connect(db_file)

# SQL query
query = """
SELECT 
    oi.order_id,
    o.order_date,
    c.first_name || ' ' || c.last_name AS customer_name,
    p.product_name,
    oi.quantity,
    oi.price_per_item,
    oi.quantity * oi.price_per_item AS total_line_price,
    c.country AS customer_country
FROM 
    OrderItems oi
    INNER JOIN Orders o ON oi.order_id = o.order_id
    INNER JOIN Customers c ON o.customer_id = c.customer_id
    INNER JOIN Products p ON oi.product_id = p.product_id
ORDER BY 
    o.order_date DESC;
"""

print("Running SQL query on ecom.db...")
print("=" * 80)
print()

# Execute query and display results using pandas for better formatting
df = pd.read_sql_query(query, conn)

# Display the results
print(f"Total rows: {len(df)}")
print()
print(df.to_string(index=False))

# Close the connection
conn.close()

print()
print("=" * 80)
print("Query execution complete!")

