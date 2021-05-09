from db import db
import users
import secrets

def addbaby(name):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "INSERT INTO babies (name, user_id) VALUES (:name, :user_id)"
    db.session.execute(sql, {"name":name, "user_id":user_id})
    db.session.commit()
    return True

def addweight(baby, weight, date):
    user_id = users.user_id()
    if user_id == 0:
        return False
    baby_id = baby
    sql = "INSERT INTO weight (baby_id, date, weight) VALUES (:baby_id, :date, :weight)"
    db.session.execute(sql, {"baby_id":baby_id, "date":date, "weight":weight})
    db.session.commit()
    return True

def addbrfeed(baby, date, duration):
    user_id = users.user_id()
    if user_id == 0:
        return False
    baby_id = baby
    sql = "INSERT INTO breastfeeding (baby_id, date, duration) VALUES (:baby_id, :date, :duration)"
    db.session.execute(sql, {"baby_id":baby_id, "date":date, "duration":duration})
    db.session.commit()
    return True

def addformula(baby, date, amount):
    user_id = users.user_id()
    if user_id == 0:
        return False
    baby_id = baby
    sql = " INSERT INTO formula (baby_id, date, amount_ml) VALUES (:baby_id, :date, :amount)"
    db.session.execute(sql, {"baby_id":baby_id, "date":date, "amount":amount})
    db.session.commit()
    return True

def addsolid(baby, date, amount, food):
    user_id = users.user_id()
    if user_id == 0:
        return False
    baby_id = baby
    sql = "INSERT INTO solid (baby_id, date, amount_gr, food) VALUES (:baby_id, :date, :amount, :food)"
    db.session.execute(sql, {"baby_id":baby_id, "date":date, "amount":amount, "food":food})
    db.session.commit()
    return True

def adddiaper(baby, date, diaper_content):
    user_id = users.user_id()
    if user_id == 0:
        return False
    baby_id = baby
    sql = "SELECT id FROM diaper_content WHERE name=:diaper_content"
    result = db.session.execute(sql, {"diaper_content":diaper_content})
    diaper_content_id = result.fetchone()
    diaper_content_id = diaper_content_id[0]
    sql = "INSERT INTO diapers (baby_id, date, diaper_content_id) VALUES (:baby_id, :date, :diaper_content_id)"
    db.session.execute(sql, {"baby_id":baby_id, "date":date, "diaper_content_id":diaper_content_id})
    db.session.commit()
    return True

def addmessage(baby, date, message):
    user_id = users.user_id()
    if user_id == 0:
        return False
    baby_id = baby
    sql = "INSERT INTO messages (user_id, baby_id, date, content) VALUES (:user_id, :baby_id, :date, :message)"
    db.session.execute(sql, {"user_id":user_id, "baby_id":baby_id, "date":date, "message":message})
    db.session.commit()
    return True

def addrights(user, baby):
    babyowner_user_id = users.user_id()
    if babyowner_user_id == 0:
        return False
    babywatcher_user_id = user
    baby_id = baby
    sql = "INSERT INTO rights (babyowner_user_id, babywatcher_user_id, baby_id) VALUES (:babyowner_user_id, :babywatcher_user_id, :baby_id)"
    db.session.execute(sql, {"babyowner_user_id":babyowner_user_id, "babywatcher_user_id":babywatcher_user_id, "baby_id":baby_id})
    db.session.commit()
    return True

def removerights(user, baby):
    babyowner_user_id = users.user_id()
    if babyowner_user_id == 0:
        return False
    babywatcher_user_id = user
    baby_id = baby
    sql = "DELETE FROM rights WHERE(babyowner_user_id=:babyowner_user_id AND babywatcher_user_id=:babywatcher_user_id AND baby_id=:baby_id)"
    db.session.execute(sql, {"babyowner_user_id":babyowner_user_id, "babywatcher_user_id":babywatcher_user_id, "baby_id":baby_id})
    db.session.commit()
    return True

def getbaby():
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "SELECT B.id, B.name FROM babies AS B JOIN rights AS R ON B.user_id = R.babyowner_user_id AND B.id = R.baby_id AND R.babywatcher_user_id=:user_id UNION SELECT id, name FROM babies WHERE user_id=:user_id;"
    baby = db.session.execute(sql, {"user_id":user_id})
    return baby.fetchall()

def getownbaby():
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "SELECT id, name FROM babies WHERE user_id=:user_id;"
    baby = db.session.execute(sql, {"user_id":user_id})
    return baby.fetchall()

def getbabyname(baby):
    user_id = users.user_id()
    if user_id == 0:
        return False
    baby_id = baby
    sql = "SELECT name FROM babies WHERE id=:baby_id;"
    baby = db.session.execute(sql, {"baby_id":baby_id})
    return baby.fetchone()

def getuser():
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "SELECT id, name FROM users"
    names = db.session.execute(sql)
    return names.fetchall()

def getrights():
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "SELECT U.name, R.babywatcher_user_id, R.baby_id, B.name FROM rights AS R, users AS U, babies AS B WHERE babyowner_user_id=:user_id AND U.id=babywatcher_user_id AND baby_id=B.id ORDER BY U.name, B.name;"
    result = db.session.execute(sql, {"user_id":user_id})
    return result.fetchall()

def getbrfeed(query):
    user_id = users.user_id()
    if user_id == 0:
        return False
    baby_id = query
    sql = "SELECT date, duration FROM breastfeeding WHERE baby_id=:baby_id ORDER BY date"
    result = db.session.execute(sql, {"baby_id":baby_id})
    return result.fetchall()

def getformula(query):
    user_id = users.user_id()
    if user_id == 0:
        return False
    baby_id = query
    sql = "SELECT date, amount_ml FROM formula WHERE baby_id=:baby_id ORDER BY date"
    result = db.session.execute(sql, {"baby_id":baby_id})
    return result.fetchall()

def getsolid(query):
    user_id = users.user_id()
    if user_id == 0:
        return False
    baby_id = query
    sql = "SELECT date, amount_gr, food FROM solid WHERE baby_id=:baby_id ORDER BY date"
    result = db.session.execute(sql, {"baby_id":baby_id})
    return result.fetchall()

def getdiaper(query):
    user_id = users.user_id()
    if user_id == 0:
        return False
    baby_id = query
    sql = "SELECT D.date, DC.name FROM diapers D, diaper_content DC WHERE D.diaper_content_id=DC.id AND baby_id=:baby_id ORDER BY date"
    result = db.session.execute(sql, {"baby_id":baby_id})
    return result.fetchall()

def getweight(query):
    user_id = users.user_id()
    if user_id == 0:
        return False
    baby_id = query
    sql = "SELECT date, weight FROM weight WHERE baby_id=:baby_id ORDER BY date"
    result = db.session.execute(sql, {"baby_id":baby_id})
    return result.fetchall()

def getmessage(query):
    user_id = users.user_id()
    if user_id == 0:
        return False
    baby_id = query
    sql = "SELECT U.name, M.date, M.content FROM messages M, users U WHERE baby_id=:baby_id AND M.user_id=U.id ORDER BY date;"
    result = db.session.execute(sql, {"baby_id":baby_id})
    return result.fetchall()