# app/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# Create function to use our app in Dev, Test or Prod
def create_app(config_type):
    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), "config", config_type + ".py")
    # /Users/kevinwalton/PycharmProjects/Milestone-3/config/dev.py - full path from code above
    app.config.from_pyfile(configuration)
    db.init_app(app)

    from app.catalog import main  # Import Blueprint
    app.register_blueprint(main)  # Register Blueprint

    return app



