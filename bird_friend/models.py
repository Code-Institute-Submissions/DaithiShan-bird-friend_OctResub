from bird_friend import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask import current_app
import os


class User(UserMixin, db.Document):
    username = db.StringField(max_length=12, unique=True, required=True)
    email = db.EmailField(max_length=100, unique=True, required=True)
    password_hash = db.StringField(required=True)
    img_url = db.URLField()

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f"User('{self.username}','{self.email}')"
