# app/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
bcrypt = Bcrypt()


# Create function to use our app in Dev, Test or Prod
def create_app(config_type):
    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), "config", config_type + ".py")
    # /Users/kevinwalton/PycharmProjects/Milestone-3/config/dev.py - full path from code above
    app.config.from_pyfile(configuration)
    db.init_app(app)  # Bind database to Flask app
    bootstrap.init_app(app)  # Initialize Bootstrap
    login_manager.init_app(app)  # Initialize LoginManager
    bcrypt.init_app(app)  # Initialize Bcrypt

    from app.catalog import main  # Import Blueprint
    app.register_blueprint(main)  # Register Blueprint

    from app.auth import authentication
    app.register_blueprint(authentication)

    return app



