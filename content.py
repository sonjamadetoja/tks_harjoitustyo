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

def addbrfeed(baby, date, duration):
    user_id = users.user_id()
    if user_id == 0:
        return False
    baby_id = baby
    sql = "INSERT INTO breastfeeding (baby_id, date, duration) VALUES (:baby_id, :date, :duration)"
    db.session.execute(sql, {"baby_id":baby_id, "date":date, "duration":duration})
    db.session.commit()
    return True

def addformula(name, date, amount):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "SELECT id FROM babies WHERE name=:name"
    result = db.session.execute(sql, {"name":name})
    baby_id = result.fetchone()
    baby_id = baby_id[0]
    sql = " INSERT INTO formula (baby_id, date, amount_ml) VALUES (:baby_id, :date, :amount)"
    db.session.execute(sql, {"baby_id":baby_id, "date":date, "amount":amount})
    db.session.commit()
    return True

def addsolid(name, date, amount, food):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "SELECT id FROM babies WHERE name=:name"
    result = db.session.execute(sql, {"name":name})
    baby_id = result.fetchone()
    baby_id = baby_id[0]
    sql = "INSERT INTO solid (baby_id, date, amount_gr, food) VALUES (:baby_id, :date, :amount, :food)"
    db.session.execute(sql, {"baby_id":baby_id, "date":date, "amount":amount, "food":food})
    db.session.commit()
    return True

def adddiaper(name, date, diaper_content):
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
    sql = "INSERT INTO diapers (baby_id, date, diaper_content_id) VALUES (:baby_id, :date, :diaper_content_id)"
    db.session.execute(sql, {"baby_id":baby_id, "date":date, "diaper_content_id":diaper_content_id})
    db.session.commit()
    return True

def addmessage(name, date, message):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "SELECT id FROM babies WHERE name=:name"
    result = db.session.execute(sql, {"name":name})
    baby_id = result.fetchone()
    baby_id = baby_id[0]
    sql = "INSERT INTO messages (baby_id, date, content) VALUES (:baby_id, :date, :message)"
    db.session.execute(sql, {"baby_id":baby_id, "date":date, "message":message})
    db.session.commit()
    return True

def addrights(user, name):
    babyowner_user_id = users.user_id()
    if babyowner_user_id == 0:
        return False
    sql = "SELECT id FROM users WHERE name=:user"
    result = db.session.execute(sql, {"user":user})
    babywatcher_user_id = result.fetchone()
    babywatcher_user_id = babywatcher_user_id[0]
    sql = "SELECT id FROM babies WHERE name=:name"
    result = db.session.execute(sql, {"name":name})
    baby_id = result.fetchone()
    baby_id = baby_id[0]
    sql = "INSERT INTO rights (babyowner_user_id, babywatcher_user_id, baby_id) VALUES (:babyowner_user_id, :babywatcher_user_id, :baby_id)"
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

def getuser():
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "SELECT name FROM users"
    names = db.session.execute(sql)
    return names.fetchall()

def getbrfeed(query):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "SELECT id FROM babies WHERE name=:query"
    result = db.session.execute(sql, {"query":query})
    baby_id = result.fetchone()
    baby_id = baby_id[0]
    sql = "SELECT date, duration FROM breastfeeding WHERE baby_id=:baby_id ORDER BY date"
    result = db.session.execute(sql, {"baby_id":baby_id})
    return result.fetchall()

def getformula(query):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "SELECT id FROM babies WHERE name=:query"
    result = db.session.execute(sql, {"query":query})
    baby_id = result.fetchone()
    baby_id = baby_id[0]
    sql = "SELECT date, amount_ml FROM formula WHERE baby_id=:baby_id ORDER BY date"
    result = db.session.execute(sql, {"baby_id":baby_id})
    return result.fetchall()

def getsolid(query):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "SELECT id FROM babies WHERE name=:query"
    result = db.session.execute(sql, {"query":query})
    baby_id = result.fetchone()
    baby_id = baby_id[0]
    sql = "SELECT date, amount_gr, food FROM solid WHERE baby_id=:baby_id ORDER BY date"
    result = db.session.execute(sql, {"baby_id":baby_id})
    return result.fetchall()

def getdiaper(query):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "SELECT id FROM babies WHERE name=:query"
    result = db.session.execute(sql, {"query":query})
    baby_id = result.fetchone()
    baby_id = baby_id[0]
    sql = "SELECT D.date, DC.name FROM diapers D, diaper_content DC WHERE D.diaper_content_id=DC.id AND baby_id=:baby_id ORDER BY date"
    result = db.session.execute(sql, {"baby_id":baby_id})
    return result.fetchall()

def getweight(query):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "SELECT id FROM babies WHERE name=:query"
    result = db.session.execute(sql, {"query":query})
    baby_id = result.fetchone()
    baby_id = baby_id[0]
    sql = "SELECT date, weight FROM weight WHERE baby_id=:baby_id ORDER BY date"
    result = db.session.execute(sql, {"baby_id":baby_id})
    return result.fetchall()

def getmessage(query):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "SELECT id FROM babies WHERE name=:query"
    result = db.session.execute(sql, {"query":query})
    baby_id = result.fetchone()
    baby_id = baby_id[0]
    sql = "SELECT date, content FROM messages WHERE baby_id=:baby_id ORDER BY date"
    result = db.session.execute(sql, {"baby_id":baby_id})
    return result.fetchall()