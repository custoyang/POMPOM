from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Pill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.String(2), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    alt_name = db.Column(db.String(100))
    dispense_time = db.Column(db.Time)
    frequency = db.Column(db.String(20), nullable=False) 
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    pills = db.relationship('Pill')
