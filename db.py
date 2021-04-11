from app import app
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from flask import session

app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
