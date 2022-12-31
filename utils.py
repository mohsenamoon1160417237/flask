import json

from sqlalchemy.ext.declarative import DeclarativeMeta
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Factory pattern
def make_app() -> Flask:
    flask_app = Flask(__name__)
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///memory.sqlite3'
    flask_app.config.from_object('config')
    return flask_app


def make_db(app: Flask) -> SQLAlchemy:
    db = SQLAlchemy(app)
    return db


class AlchemyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if
                          not x.startswith('_') and x != 'metadata' and x in ["free", "total", "id", "used"]]:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data)  # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)
