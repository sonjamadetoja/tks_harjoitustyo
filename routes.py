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
        password2 = request.form["password2"]
        if password != password2:
            return render_template("error.html", message="Salasanat eivät täsmää.")
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
        return redirect("/add")
    else:
        return render_template("error.html", message="routes/addbaby")

@app.route("/addweight", methods=["post"])
def addweight():
    name = request.form["name"]
    weight = request.form["weight"]
    date = request.form["date"]
    if content.addweight(name, weight, date):
        return redirect("/add")
    else: 
        return render_template("error.html", message="routes/addweight")

@app.route("/addbrfeed", methods=["post"])
def addbrfeed():
    name = request.form["name"]
    date = request.form["date"]
    start_time = request.form["start_time"]
    duration = request.form["duration"]
    if content.addbrfeed(name, date, start_time, duration):
        return redirect("/add")
    else: 
        return render_template("error.html", message="routes/addbrfeed")

@app.route("/addformula", methods=["post"])
def addformula():
    name = request.form["name"]
    date = request.form["date"]
    start_time = request.form["start_time"]
    amount = request.form["amount"]
    if content.addformula(name, date, start_time, amount):
        return redirect("/add")
    else: 
        return render_template("error.html", message="routes/addformula")

@app.route("/addsolid", methods=["post"])
def addsolid():
    name = request.form["name"]
    food = request.form["food"]
    amount = request.form["amount"]
    date = request.form["date"]
    start_time = request.form["start_time"]
    if content.addsolid(name, date, start_time, amount, food):
        return redirect("/add")
    else: 
        return render_template("error.html", message="routes/addsolid")

@app.route("/adddiaper", methods=["post"])
def adddiaper():
    name = request.form["name"]
    diaper_content = request.form["diaper"]
    date = request.form["date"]
    time = request.form["time"]
    if content.adddiaper(name, date, time, diaper_content):
        return redirect("/add")
    else: 
        return render_template("error.html", message="routes/adddiaper")