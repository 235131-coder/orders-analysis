import sqlite3

conn = sqlite3.connect("orders.db")
cur = conn.cursor()

cur.executescript("""
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    city TEXT
);

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    amount INTEGER,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

INSERT INTO customers VALUES
(1, 'Ali', 'Islamabad'),
(2, 'Sara', 'Lahore'),
(3, 'Bilal', 'Islamabad'),
(4, 'Ayesha', 'Karachi'),
(5, 'Usman', 'Lahore'),
(6, 'Zain', 'Peshawar');

INSERT INTO orders VALUES
(101, 1, 4500), (102, 1, 7200),
(103, 2, 3000), (104, 3, 9800),
(105, 4, 2500), (106, 4, 1500),
(107, 5, 5800), (108, 5, 6200),
(109, 6, 1200), (110, 3, 500);
""")

conn.commit()
conn.close()
print("Database created successfully.")