from flask import Flask,render_template,request,redirect,url_for,flash
from database import get_products,get_sales,get_stock,insert_products,insert_sales,insert_stock,check_user_exists,get_users,insert_users


app = Flask(__name__)

app.secret_key = 'wowoyayywowy'


# http://127.0.0.1:5000/
@app.route('/') 
def home():
    return render_template('index.html')


# http://127.0.0.1:5000/products
@app.route('/products')
def products():
    products_data = get_products()
    return render_template('products.html',products_data = products_data)


@app.route('/add_product',methods=['GET','POST'])
def add_product():
    if request.method == 'POST':
        product_name = request.form['p_name']
        buying_price = request.form['b_price']
        selling_price = request.form['s_price']
        new_product = (product_name,buying_price,selling_price)
        insert_products(new_product)
        flash("Product added successfully",'success')
    return redirect(url_for('products'))


@app.route('/sales')
def sales():
    sales_data = get_sales()
    products_data = get_products()
    return render_template('sales.html',sales_data = sales_data,products_data = products_data)


@app.route('/add_sale',methods=['GET','POST'])
def add_sale():
    if request.method == 'POST':
        product_id = request.form['p_id']
        quantity = request.form['quantity']
        new_sale = (product_id,quantity)
        insert_sales(new_sale)
        flash("Sale added successfully",'success')
    return redirect(url_for('sales'))


@app.route('/stock')
def stock():
    stock_data = get_stock()
    products_data = get_products()
    return render_template('stock.html',stock_data = stock_data,products_data = products_data)


@app.route('/add_stock',methods=['GET','POST'])
def add_stock():
    if request.method == 'POST':
        product_id = request.form['p_id']
        stock_quantity = request.form['stock_quantity']
        new_stock = (product_id,stock_quantity)
        insert_stock(new_stock)
        flash("Stock added successfully",'success')
    return redirect(url_for('stock'))

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html',)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    users_data = get_users()
    return render_template('register.html',users_data = users_data)


@app.route('/register_here',methods=['GET','POST'])
def register_here():
    if request.method == 'POST':
        email = request.form['email']
        if check_user_exists(email):
            flash("User already exists",'danger')
            return redirect(url_for('register'))
        else:
            full_name = request.form['f_name']
            phone_number = request.form['phone_number']
            password = request.form['password']
            new_user = (full_name,email,phone_number,password)
            insert_users(new_user)
            flash("Account created successfully",'success')
    return redirect(url_for('register'))


app.run(debug=True)