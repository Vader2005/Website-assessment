from flask import Blueprint

auth = Blueprint('auth', __name__)

# Create the login url

@auth.route('/login')
def login():
    return "<p> Login </p>"

# Create the logout url

@auth.route('/logout')
def logout():
    return "<p> Logout </p>"

# Create the sign-up url

@auth.route('/sign-up')
def sign_up():
    return "<p> Sign Up </p>"


