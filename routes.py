from app import app
from flask import redirect, render_template, request, session
import db, content, users

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["get", "post"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["name"]
        password = request.form["password"]
        if users.register(username, password):
            return redirect("/main")
        else:
            return render_template("error.html", message="routes/register")

@app.route("/login", methods=["get", "post"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["name"]
        password = request.form["password"]
        if users.login(username,password):
            return redirect("/main")
        else:
            return render_template("error.html", message="routes/login")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/main")
def main():
    return render_template("main.html")

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/addbaby", methods=["post"])
def addbaby():
    name = request.form["name"]
    if content.addbaby(name):
        return redirect("/main")
    else:
        return render_template("error.html", message="routes/addbaby")

@app.route("/addweight", methods=["post"])
def addweight():
    name = request.form["name"]
    weight = request.form["weight"]
    date = request.form["date"]
    if content.addweight(name, weight, date):
        return redirect("/main")
    else: 
        return render_template("error.html", message="routes/addweight")