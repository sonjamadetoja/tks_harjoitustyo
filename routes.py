from app import app
from flask import redirect, render_template, request, session
import db, content, users

from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader('app', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)


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
        if users.getuser(username):
            return render_template("error.html", message="Tämä käyttäjänimi on jo käytössä.")
        if password != password2:
            return render_template("error.html", message="Salasanat eivät täsmää.")
        if users.register(username, password):
            return redirect("/main")
        else:
            return render_template("error.html", message="Rekisteröityminen ei onnistunut.")

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
            return render_template("error.html", message="Sisäänkirjautuminen ei onnistunut. Tarkista tunnus ja salasana.")

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
        return render_template("error.html", message="Vauvan lisääminen ei onnistunut.")

@app.route("/addweight", methods=["post"])
def addweight():
    name = request.form["name"]
    weight = request.form["weight"]
    date = request.form["date"]
    if content.addweight(name, weight, date):
        return redirect("/add")
    else: 
        return render_template("error.html", message="Painon lisääminen ei onnistunut.")

@app.route("/addbrfeed", methods=["post"])
def addbrfeed():
    name = request.form["name"]
    date = request.form["date"]
    start_time = request.form["start_time"]
    date = date + " " + start_time
    duration = request.form["duration"]
    if content.addbrfeed(name, date, duration):
        return redirect("/add")
    else: 
        return render_template("error.html", message="Imetyksen lisääminen ei onnistunut.")

@app.route("/addformula", methods=["post"])
def addformula():
    name = request.form["name"]
    date = request.form["date"]
    start_time = request.form["start_time"]
    date = date + " " + start_time
    amount = request.form["amount"]
    if content.addformula(name, date, amount):
        return redirect("/add")
    else: 
        return render_template("error.html", message="Korvikkeen lisääminen ei onnistunut.")

@app.route("/addsolid", methods=["post"])
def addsolid():
    name = request.form["name"]
    food = request.form["food"]
    amount = request.form["amount"]
    date = request.form["date"]
    start_time = request.form["start_time"]
    date = date + " " + start_time
    if content.addsolid(name, date, amount, food):
        return redirect("/add")
    else: 
        return render_template("error.html", message="Kiinteän ruuan lisääminen ei onnistunut.")

@app.route("/adddiaper", methods=["post"])
def adddiaper():
    name = request.form["name"]
    diaper_content = request.form["diaper"]
    date = request.form["date"]
    time = request.form["time"]
    date = date + " " + time
    if content.adddiaper(name, date, diaper_content):
        return redirect("/add")
    else: 
        return render_template("error.html", message="Vaipanvaihdon lisääminen ei onnistunut.")

@app.route("/browse")
def browse():
    list = content.getbaby()
    new_list = []
    for row in list:
        new_list.append(row[0])
    return render_template("browse.html", list=new_list)

@app.route("/search", methods=["get"])
def search():
    query = request.args["query"]
    list = content.getbrfeed(query)
    brfeed = []
    for row in list:
        tpl = "Pvm: "+row[0].strftime('%d.%m.%Y, klo: %H:%M') + ", kesto: "+row[1]+" min"
        brfeed.append(tpl)
    list = content.getformula(query)
    formula = []
    for row in list:
        tpl = "Pvm: "+row[0].strftime('%d.%m.%Y, klo: %H:%M') + ", määrä: "+str(row[1])+" ml"
        formula.append(tpl)
    list = content.getsolid(query)
    solid = []
    for row in list:
        tpl = "Pvm: "+row[0].strftime('%d.%m.%Y, klo: %H:%M') + ", määrä: "+str(row[1])+" g" + ", ruoka: " + row[2]
        solid.append(tpl)
    list = content.getdiaper(query)
    diapers = []
    for row in list:
        tpl = "Pvm: "+row[0].strftime('%d.%m.%Y') + ", sisältö: "+str(row[1])
        diapers.append(tpl)
    list = content.getweight(query)
    weight = []
    for row in list:
        tpl = "Pvm: "+row[0].strftime('%d.%m.%Y') + ", paino: "+str(row[1])+" g"
        weight.append(tpl)
    return render_template("result.html", query=query, brfeed=brfeed, formula=formula, solid=solid, weight=weight, diapers=diapers)
