from db import db
from flask import abort, request, session, render_template
from werkzeug.security import check_password_hash, generate_password_hash
import os

def login(name,password):
    sql = "SELECT password, id FROM users WHERE name=:name"
    result = db.session.execute(sql, {"name":name})
    user = result.fetchone()
    if user == None:
        return False
    else:
        if check_password_hash(user[0],password):
            session["user_id"] = user[1]
            session["username"] = name
            return True
        else:
            return False

def logout():
    del session["user_id"]

def user_id():
    return session.get("user_id",0)


def register(name,password):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (name,password) VALUES (:name,:password)"
        db.session.execute(sql, {"name":name,"password":hash_value})
        db.session.commit()
    except:
        return render_template("error.html", message="users/register")
    return login(name,password)

