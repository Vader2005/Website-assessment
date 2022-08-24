from flask import Blueprint

# All things not related to authentication
# What display on the home page, and the designated url for that home page

views = Blueprint('views', __name__)

@views.route('/')

def home():
    return "<h1> Test </h1>"

