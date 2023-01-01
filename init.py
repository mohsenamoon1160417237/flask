from flask_sqlalchemy import SQLAlchemy
from main_app import flask_app

with flask_app.app_context():
    db = SQLAlchemy(flask_app)
    db.create_all()
