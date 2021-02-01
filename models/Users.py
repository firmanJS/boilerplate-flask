from models import BaseModel
from helpers.postgre_alchemy import postgre_alchemy as db
from flask import Flask
app = Flask(__name__)
class UsersModel(BaseModel, db.Model):
    """Model for the users table"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    name = db.Column(db.String(125))
    last_login = db.Column(db.DateTime(True))
    createdAt = db.Column(db.DateTime(True), default=db.func.now())
    updatedAt = db.Column(db.DateTime(True), default=db.func.now())
    is_active = db.Column(db.Boolean, default=False)
    is_deleted = db.Column(db.Boolean, default=False)


def __init__(self, username, password):
    self.username = username
    self.password = password

with app.app_context():
    db.create_all()
