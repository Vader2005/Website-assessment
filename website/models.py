# databse model for the users:

from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    # Define all the columns for the database table
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True) # 150 is the max string length, no user can have the same email as the other user
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
