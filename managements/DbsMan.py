from flask_sqlalchemy import SQLAlchemy

from main_app import flask_app


class DbsMan:
    db_memory = None
    my_db = None

    @staticmethod
    def get_db_memory():
        if not DbsMan.db_memory:
            DbsMan.db_memory = SQLAlchemy(flask_app)
        return DbsMan.db_memory

    @classmethod
    def make_tbl(cls):
        cls.my_db.create_all()
