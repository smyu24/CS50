import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session, g, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from functools import wraps

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

# Configure application
app = Flask(__name__)

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///MYP.db")

@app.route("/")
def index():
    """Show the main page"""
    # TODO this will be the main page of the website after the user has logged in:
    print(session["user_id"])
    if len(session["user_id"]) == 0:
        return render_template("login.html")#abort
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return flash("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return flash("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return flash("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""
    # Forget any user_id
    session.clear()
    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        if not request.form.get("username"): #if username isn't provided
            return flash("Must Input A Username")
        elif not request.form.get("password"):
            return flash("Must Provide Password")
        elif not request.form.get("confirmation"): #if password comfirmation isn't provided
            return flash("Must Provide Password Confirmation")
        elif request.form.get("password") != request.form.get("confirmation"): #password and confirmation must match
            return flash("Passwords Must Match")

        #hash user's password
        hash = generate_password_hash(request.form.get("password"))
        user_name = request.form.get("username")
        #add user into database if they pass all restrictions
        U = db.execute("SELECT username FROM users WHERE username=:username", username=user_name)
        if len(U) != 0:
            return flash("Username is already in use")

        data = db.execute("INSERT INTO users (username, hash) VALUES(:username, :hash)", username=user_name, hash=hash)

        session["user_id"] = data

        # redirect the user
        return redirect("/")#later change to index.html
    else:
        return render_template("register.html")

app.route("/info", methods=["GET", "POST"]) # change to something else
@login_required
def info(): # change to something else
    """Something"""
    if request.method == "POST":
        return redirect("/")
    else:
        return render_template("")

app.route("/userform", methods=["GET", "POST"]) # change to something else
@login_required
def userform(): # change to something else
    """Something"""
    if request.method == "POST":
        return redirect("/")
    else:
        return render_template("")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return flash(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
