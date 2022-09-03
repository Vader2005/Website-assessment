from flask import Blueprint, render_template, request, flash, redirect, url_for, json
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash # To secure password, hashing function is a one eay function, where it does not have an inverse
from .models import db
import sys

auth = Blueprint('auth', __name__)

# Create the login url

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

# Create the logout url

@auth.route('/logout')
def logout():
    return "<p> Logout </p>"

# Create the sign-up url

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        #print("THE POST REQUEST WORKS!!!!!!!!!!!!!")
        # Load the data from the form
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password = request.form.get('password')

        new_user = User(email=email, first_name=first_name, password=generate_password_hash(password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        print("Your account has been created!!!!!!!")
        return redirect(url_for('views.home'))

    return render_template('sign-up.html')

