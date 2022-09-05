from flask import Blueprint, render_template, request, flash, redirect, url_for, json
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash # To secure password, hashing function is a one eay function, where it does not have an inverse
from .models import db
import sys
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

# Create the login url

@auth.route('/login', methods=['GET', 'POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    if request.method == 'POST':
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                print("Login successful!!!!!!!!!!!!!!!!!!!!")
                login_user(user, remember=True) # Basically logs in the user and stores in the flask session
                return redirect(url_for('views.home'))
            else:
                print("Incorrect password, try again!!!!!!!")
        else:
            print("User does not exist!!!!!!!!!!!")

    return render_template('login.html')

# Create the logout url

@auth.route('/logout')
@login_required # Makes sure we can't access the page or route unless the user is logged in
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

# Create the sign-up url

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        #print("THE POST REQUEST WORKS!!!!!!!!!!!!!")
        # Load the data from the form
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        new_user = User(email=email, first_name=first_name, password=generate_password_hash(password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        login_user(user, remember=True) 
        print("Your account has been created!!!!!!!")
        return redirect(url_for('views.home'))
    
    return render_template('sign-up.html')

