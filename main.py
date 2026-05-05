from flask import Flask,render_template,request,redirect,url_for,flash
from database import get_products,get_sales,get_stock,insert_products,insert_sales,insert_stock,check_user_exists,get_users,insert_users
from flask_bcrypt import Bcrypt
from functools import wraps

app = Flask(__name__)


bcrypt = Bcrypt(app)

app.secret_key = 'wowoyayywowy'


# http://127.0.0.1:5000/
@app.route('/') 
def home():
    return render_template('index.html')



def login_required(f):
    @wraps(f)
    def protected(*args,**kwargs):
        if 'email' not in session:
            return redirect(url_for('login'))
        return f(*args,**kwargs)
    return protected


# http://127.0.0.1:5000/products
@app.route('/products')
def products():
    products_data = get_products()
    return render_template('products.html',products_data = products_data)


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
@login_required
def dashboard():
    return render_template('dashboard.html',)

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        existing_user = check_user_exists(email)
        if not existing_user:
            flash("User doesn't exist, please register",'danger')
        else:
            if bcrypt.check_password_hash(existing_user[-1],password):
                session['email'] = email
                flash("Login successful",'success')
                return redirect(url_for('dashboard'))
            else:
                flash("Password incorrect",'danger')
    return render_template('login.html')


@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        full_name = request.form['f_name']
        email = request.form['email']
        phone_number = request.form['phone_number']
        password = request.form['password']
        
        existing_user = check_user_exists(email)
        if not existing_user:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            new_user = (full_name,email,phone_number,hashed_password)
            insert_users(new_user)
            flash("Account created successfully",'success')
        else:
            flash("User already exists",'danger')
    return render_template('register.html')

#log out by removing email in session
@app.route('/logout')
def logout():
    session.pop('email',None)
    flash("Logged out successfully",'success')
    return redirect(url_for('login'))



app.run(debug=True)