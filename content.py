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