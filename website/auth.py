from flask import Blueprint, render_template, request, flash

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
    return render_template('sign-up.html')


