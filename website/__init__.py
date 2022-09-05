from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

# Initialize the database
db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    # Creating the app instance

    app = Flask(__name__)
    app.config['SECRET KEY'] = 'edjhdefehfej'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # Telling flask where the database is stores
    #app.secret_key = 'edjhdefehfej'
    db.init_app(app) # Initialize the databse

    # registering the views from views.py and auth.py

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User # Making sure we load the database file

    create_database(app)

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print("Created database!")

# This is the package file of the website, this is where i registered the views and created the app instance

