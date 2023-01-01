from flask_sqlalchemy import SQLAlchemy

from main_app import flask_app


class DbsMan:

    dbMemory = None
    __myDb__ = None

    @staticmethod
    def readyDbMemory():
        if not DbsMan.dbMemory:
            DbsMan.dbMemory = SQLAlchemy(flask_app)


    @classmethod
    def makeTbl(cls):
        cls.__myDb__.create_all()
