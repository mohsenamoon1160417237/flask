import json

from flask_sqlalchemy import SQLAlchemy
from flask import request
from utils import AlchemyEncoder

from memory_data import flask_app
from views.RamCtrl import RamCtrl

db = SQLAlchemy(flask_app)


if __name__ == "__main__":
    flask_app.run(debug=True)
