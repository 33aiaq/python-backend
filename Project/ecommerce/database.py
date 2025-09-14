import sqlite3

DB_NAME = "store.db"

# -------------------- INIT --------------------
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    # Create products table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        stock INTEGER NOT NULL,
        type TEXT NOT NULL,
        extra_info TEXT
    )
    """)

    # Create users table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)

    # Create orders table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        total REAL NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    """)

    conn.commit()
    conn.close()

# -------------------- PRODUCT FUNCTIONS --------------------
def add_product(name, price, stock, type_, extra_info=""):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("INSERT INTO products (name, price, stock, type, extra_info) VALUES (?, ?, ?, ?, ?)",
                (name, price, stock, type_, extra_info))
    conn.commit()
    conn.close()

def get_products():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT id, name, price, stock, type, extra_info FROM products")
    products = cur.fetchall()
    conn.close()
    return products

def update_stock(product_id, new_stock):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("UPDATE products SET stock = ? WHERE id = ?", (new_stock, product_id))
    conn.commit()
    conn.close()

# -------------------- USER FUNCTIONS --------------------
def add_user(username, password_hash):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password_hash))
    conn.commit()
    conn.close()

def get_user(username):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT id, username, password FROM users WHERE username = ?", (username,))
    row = cur.fetchone()
    conn.close()
    return row  # (id, username, password) or None

# -------------------- ORDER FUNCTIONS --------------------
def add_order(user_id, total):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("INSERT INTO orders (user_id, total) VALUES (?, ?)", (user_id, total))
    conn.commit()
    conn.close()

def get_orders(user_id):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT id, total FROM orders WHERE user_id = ?", (user_id,))
    orders = cur.fetchall()
    conn.close()
    return orders

# -------------------- RUN ONCE --------------------
if __name__ == "__main__":
    init_db()

    # Sample products
    add_product("Python 101", 30, 10, "Book", "John Doe")
    add_product("Data Science Handbook", 40, 5, "Book", "Jane Smith")
    add_product("Laptop", 1200, 3, "Electronics", "Dell")
    add_product("Smartphone", 800, 7, "Electronics", "Samsung")
    add_product("Wireless Earbuds", 150, 15, "Electronics", "Sony")
    add_product("Smartwatch", 200, 10, "Electronics", "Apple")
    add_product("Tablet", 400, 5, "Electronics", "Lenovo")
    add_product("T-Shirt", 20, 25, "Clothing", "M")
    add_product("Jeans", 40, 15, "Clothing", "L")
    add_product("Jacket", 60, 10, "Clothing", "XL")

    print("Database initialized and sample products added.")
