import os
from datetime import datetime
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps


app = Flask(__name__)

# Database setup
db = SQL("sqlite:///inventory.db")
db.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL UNIQUE,
        hash TEXT NOT NULL,
        username TEXT 
    )
""")

app.secret_key = os.environ.get("SECRET_KEY") or "supersecretkey"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

def login_required(f):  
    @wraps(f)  
    def decorated_function(*args, **kwargs): 
        if "user_id" not in session:
            flash("Please log in first.", "danger") 
            return redirect(url_for("login"))  
        return f(*args, **kwargs)  
    return decorated_function  

@app.route("/")
def index():
    return redirect(url_for('login'))  

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email").strip().lower()
        password = request.form.get("password")
       

        if not email or not password:
            flash("Can't Leave Forms Empty", "danger")
            return redirect(url_for('login'))

        check = db.execute("SELECT * FROM users WHERE email = ?", email)

        if not check:
            flash("Email Not Registered", "danger")
            return redirect(url_for('login'))

        user_hash = check[0]["hash"]

        if not check_password_hash(user_hash, password):
            flash("Invalid Password", "danger")
            return redirect(url_for('login'))
        
        session["user_id"] = check[0]["id"]

        flash("Logged in Successfully", "success")
        return redirect(url_for('home'))  

    return render_template("store/login.html")  

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email").strip().lower()
        password = request.form.get("password")
        passagain = request.form.get("passagain")
        user = request.form.get("user")


        if not email or not password or not passagain or not user:
            flash("Can't Leave Forms Empty", "danger")
            return redirect(url_for('register'))

        if len(password) < 8:
            flash("Password must be at least 8 characters", "danger")
            return redirect(url_for('register'))

        usercheck = db.execute("SELECT email FROM users WHERE email = ?", email)

        if usercheck:
            flash("Email already in use", "danger")
            return redirect(url_for('register'))

        if password != passagain:
            flash("Passwords Don't Match", "danger")
            return redirect(url_for('register'))

        try:
            db.execute("INSERT INTO users (email, hash, username) VALUES (?, ?, ?)", email, generate_password_hash(password), user)
        except Exception as e:
            flash("Registration failed due to a server error", "danger")
            return redirect(url_for('register'))

        flash("Registered successfully! You can log in now.", "success")
        return redirect(url_for('login'))

    return render_template("store/register.html")

@app.route("/forget", methods=["GET", "POST"])
def forget():
    if request.method == "POST":
        email = request.form.get("email").strip().lower()
        nwpassword = request.form.get("password")
        passagain = request.form.get("passagain")

        if not email or not nwpassword or not passagain:
            flash("Fill the form", "danger")
            return redirect(url_for('forget'))

        checkmail = db.execute("SELECT * FROM users WHERE email = ?", email)

        if not checkmail:
            flash("Email not registered", "danger")
            return redirect(url_for('forget'))

        if nwpassword != passagain:
            flash("Passwords don't match", "danger")
            return redirect(url_for('forget'))
        
        if len(nwpassword) < 8:
            flash("Passwords must be at least 8 characters", "danger")
            return redirect(url_for('forget'))
        
        if checkmail:
            try:
                db.execute("UPDATE users SET hash = ? WHERE email = ?", generate_password_hash(nwpassword), email)
                flash("Password reset successfully! Please log in.", "success")
                return redirect(url_for('login'))
            except Exception as e:
                flash("Failed to reset password due to a server error", "danger")
                return redirect(url_for('forget'))

    return render_template("store/forget.html")


@app.route("/logout")
@login_required
def logout():
        session.clear()
        return redirect("/")


@app.route("/home")
@login_required  
def home():
    user_id = session.get("user_id")
    user = db.execute("SELECT username FROM users WHERE id = ? ", user_id)[0]["username"]

    return render_template("store/home.html", username=user)




@app.route("/inventory", methods=["GET","POST"])
@login_required
def inventory():
    user_id = session.get("user_id")
    items = db.execute("SELECT * FROM inventory WHERE user_id = ?", user_id)
    
    return render_template("store/inventory.html", items=items)
    


@app.route("/add_item", methods=["POST"])
@login_required
def add_item():
    name = request.form.get("name")
    price = request.form.get("price")
    stock = request.form.get("stock")

    if not name or not price or not stock:
        flash("Must Provide Product/Service details", "danger")
        return redirect(url_for('inventory'))
    
    db.execute("INSERT INTO inventory (name, price, stock) VALUES (?, ?, ?)", (name, price, stock))
    db.commit()

    flash ("Item added!","success")
    return redirect("/inventory")

@app.route("/orders")
@login_required
def orders():

    return render_template("store/orders.html")
    





@app.route("/dashboard")
@login_required
def dashboard():
    
    return render_template("store/dashboard.html")
    






if __name__ == "__main__":
     app.run(debug=True)