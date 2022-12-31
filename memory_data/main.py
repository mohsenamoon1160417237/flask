import json

from flask_sqlalchemy import SQLAlchemy
from flask import request
from utils import AlchemyEncoder

from memory_data import flask_app

db = SQLAlchemy(flask_app)


class MemoryData(db.Model):
    __tablename__ = "memory_data"

    serialize_only = ('id', 'total', 'free', 'used',)

    id = db.Column('memory_data_id', db.Integer, primary_key=True)
    total = db.Column(db.Float)
    free = db.Column(db.Float)
    used = db.Column(db.Float)

    def __init__(self, total, free, used):
        self.total = total
        self.free = free
        self.used = used

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


@flask_app.route('/')
def view():
    n = request.args.get('n')
    if n is not None:
        n = int(n)
        memory_datas = MemoryData.query.all()[::-1][:n]
    else:
        memory_datas = MemoryData.query.all()
    return json.dumps(memory_datas, cls=AlchemyEncoder)
    # return memory_datas.to_dict()
    # return memory_datas


if __name__ == "__main__":
    flask_app.run(debug=True)
