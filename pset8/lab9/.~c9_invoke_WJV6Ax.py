import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///MYP.db")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # TODO: Add the user's entry into the database
        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")
        if len(request.form.get("name")) or len(request.form.get("month")) or len(request.form.get("day")) != 0:
            db.execute("INSERT INTO birthdays (name, month, day) VALUES (:name, :month, :day)", name=name, month=month, day=day)
        return redirect("/")
    else: # if the request.method is not "POST" but rather "GET"
        # TODO: Display the entries in the database on index.html
        info = db.execute("SELECT name, month, day FROM birthdays")
        return render_template("index.html", info=info, index=index)


