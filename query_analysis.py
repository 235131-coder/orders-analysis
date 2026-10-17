import sqlite3

conn = sqlite3.connect("orders.db")
cur = conn.cursor()

# (a) INNER JOIN query
print("--- Customer orders (joined) ---")
cur.execute("""
SELECT c.name, o.amount 
FROM customers c 
INNER JOIN orders o ON c.customer_id = o.customer_id;
""")
for row in cur.fetchall():
    print(row)

# (b) GROUP BY total spend per customer
print("\n--- Total spend per customer ---")
cur.execute("""
SELECT c.name, SUM(o.amount) AS total_spend 
FROM customers c 
JOIN orders o ON c.customer_id = o.customer_id 
GROUP BY c.customer_id 
ORDER BY total_spend DESC;
""")
for row in cur.fetchall():
    print(row)

conn.close()