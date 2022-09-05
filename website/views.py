from flask import Blueprint, render_template
from flask_login import login_required, current_user

# All things not related to authentication
# What display on the home page, and the designated url for that home page

views = Blueprint('views', __name__)

@views.route('/')
@login_required # Now you can't get to the home page unless you login
def home():
    return render_template('main.html')

