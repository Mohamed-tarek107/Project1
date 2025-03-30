
import os
from datetime import datetime
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash



app = Flask(__name__)
db = SQL("sqlite:///inventory.db")
app.secret_key = "supersecretkey" # for the flash to work "dont erase" 


@app.route("/")
def index():
    return redirect(url_for('login'))  



@app.route("/login", methods=["GET", "POST"])
def login():
    
    if request.method == "POST":
        email = request.form.get("email")
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
        email = request.form.get("email")
        password = request.form.get("password")
        passagain = request.form.get("passagain")

        if not email or not password or not passagain:
            flash("Can't Leave Forms Empty", "danger")
            return redirect(url_for('register'))

        usercheck = db.execute("SELECT email FROM users WHERE email = ?", email)

        if usercheck:
            flash("Email already in use", "danger")
            return redirect(url_for('register'))

        if password != passagain:
            flash("Passwords Don't Match", "danger")
            return redirect(url_for('register'))

        db.execute("INSERT INTO users (email, hash) VALUES (?, ?)", email, generate_password_hash(password))
        flash("Registered successfully! You can log in now.", "success")
        return redirect(url_for('login'))

    return render_template("store/register.html")


@app.route("/forget", methods=["GET","POST"])
def forget():
    return render_template("store/forget.html")


@app.route("/home", methods=["GET","POST"])
def home():
    return render_template("store/home.html")








if __name__ == "__main__":
    app.run(debug=True)
