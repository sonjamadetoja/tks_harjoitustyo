from db import db
import users

def addbaby(name):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "INSERT INTO babies (name, user_id) VALUES (:name, :user_id)"
    db.session.execute(sql, {"name":name, "user_id":user_id})
    db.session.commit()
    return True

def addweight(name, weight, date):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "SELECT id FROM babies WHERE name=:name"
    result = db.session.execute(sql, {"name":name})
    baby_id = result.fetchone()
    baby_id = baby_id[0]
    sql = "INSERT INTO weight (baby_id, date, weight) VALUES (:baby_id, :date, :weight)"
    db.session.execute(sql, {"baby_id":baby_id, "date":date, "weight":weight})
    db.session.commit()
    return True

def addbrfeed(name, date, time, duration):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "SELECT id FROM babies WHERE name=:name"
    result = db.session.execute(sql, {"name":name})
    baby_id = result.fetchone()
    baby_id = baby_id[0]
    sql = " INSERT INTO breastfeeding (baby_id, date, time, duration) VALUES (:baby_id, :date, :time, :duration)"
    db.session.execute(sql, {"baby_id":baby_id, "date":date, "time":time, "duration":duration})
    db.session.commit()
    return True

def addformula(name, date, time, amount):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "SELECT id FROM babies WHERE name=:name"
    result = db.session.execute(sql, {"name":name})
    baby_id = result.fetchone()
    baby_id = baby_id[0]
    sql = " INSERT INTO formula (baby_id, date, time, amount_ml) VALUES (:baby_id, :date, :time, :amount)"
    db.session.execute(sql, {"baby_id":baby_id, "date":date, "time":time, "amount":amount})
    db.session.commit()
    return True

def addsolid(name, date, time, amount, food):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "SELECT id FROM babies WHERE name=:name"
    result = db.session.execute(sql, {"name":name})
    baby_id = result.fetchone()
    baby_id = baby_id[0]
    sql = "INSERT INTO solid (baby_id, date, time, amount_gr, food) VALUES (:baby_id, :date, :time, :amount, :food)"
    db.session.execute(sql, {"baby_id":baby_id, "date":date, "time":time, "amount":amount, "food":food})
    db.session.commit()
    return True

def adddiaper(name, date, time, diaper_content):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "SELECT id FROM babies WHERE name=:name"
    result = db.session.execute(sql, {"name":name})
    baby_id = result.fetchone()
    baby_id = baby_id[0]
    sql = "SELECT id FROM diaper_content WHERE name=:diaper_content"
    result = db.session.execute(sql, {"diaper_content":diaper_content})
    diaper_content_id = result.fetchone()
    diaper_content_id = diaper_content_id[0]
    sql = "INSERT INTO diapers (baby_id, date, time, diaper_content_id) VALUES (:baby_id, :date, :time, :diaper_content_id)"
    db.session.execute(sql, {"baby_id":baby_id, "date":date, "time":time, "diaper_content_id":diaper_content_id})
    db.session.commit()
    return True
