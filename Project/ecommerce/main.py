from flask import Flask, render_template, request, redirect, url_for, session
from products import Book, Electronics, Clothing
from models import User
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "your_secret_key_here"

# ------------------ PRODUCTS ------------------
products = [
    # Books (2)
    Book("Python 101", 30, 10, "John Doe"),
    Book("Data Science Handbook", 40, 5, "Jane Smith"),

    # Electronics (5)
    Electronics("Laptop", 1200, 3, "Dell"),
    Electronics("Smartphone", 800, 7, "Samsung"),
    Electronics("Wireless Earbuds", 150, 15, "Sony"),
    Electronics("Smartwatch", 200, 10, "Apple"),
    Electronics("Tablet", 400, 5, "Lenovo"),

    # Clothing (3)
    Clothing("T-Shirt", 20, 25, "M"),
    Clothing("Jeans", 40, 15, "L"),
    Clothing("Jacket", 60, 10, "XL")
]

# ------------------ USERS ------------------
users = {}

# ------------------ ROUTES ------------------
@app.route('/')
def home():
    return redirect(url_for('login'))

# ------------------ REGISTER ------------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']
        if not username or not password:
            error = "Username and password are required."
        elif username in users:
            error = "Username already exists."
        else:
            password_hash = generate_password_hash(password)
            users[username] = {'object': User(username), 'password': password_hash}
            session['username'] = username
            return redirect(url_for('index'))
    return render_template('register.html', error=error)

# ------------------ LOGIN ------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']
        if username not in users or not check_password_hash(users[username]['password'], password):
            error = "Invalid username or password."
        else:
            session['username'] = username
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

# ------------------ LOGOUT ------------------
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

# ------------------ INDEX ------------------
@app.route('/index')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('index.html', products=products, error=None, username=session['username'])

# ------------------ ADD TO CART ------------------
@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    if 'username' not in session:
        return redirect(url_for('login'))
    username = session['username']
    user = users[username]['object']

    product_name = request.form['product_name']
    quantity = int(request.form['quantity'])
    error_msg = None

    for p in products:
        if p.name == product_name:
            if quantity > p._stock:
                error_msg = f"Warning: Only {p._stock} items in stock."
            else:
                user.cart.add_product(p, quantity)
            break

    return render_template('index.html', products=products, error=error_msg, username=session['username'])

# ------------------ CART ------------------
@app.route('/cart')
def cart():
    if 'username' not in session:
        return redirect(url_for('login'))
    user = users[session['username']]['object']
    items = user.cart.view_cart()
    return render_template('cart.html', cart=items, total=user.cart.total(), username=session['username'])

# ------------------ CHECKOUT ------------------
@app.route('/checkout')
def checkout():
    if 'username' not in session:
        return redirect(url_for('login'))
    user = users[session['username']]['object']
    total_amount = user.checkout()
    return render_template('checkout.html', user=user, total=total_amount, username=session['username'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
