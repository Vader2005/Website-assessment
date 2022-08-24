from flask import Flask

def create_app():
    # Creating the app instance

    app = Flask(__name__)
    app.config['SECRET KEY'] = 'edjhdefehfej'

    # registering the views from views.py and auth.py

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app

# This is the package file of the website, this is where i registered the views and created the app instance

