from flask_sqlalchemy import SQLAlchemy

from main_app import flask_app


class DbsMan:

    dbMemory = None
    myDb = None

    @staticmethod
    def getDbMemory():
        if not DbsMan.dbMemory:
            DbsMan.dbMemory = SQLAlchemy(flask_app)
        return DbsMan.dbMemory


    @classmethod
    def makeTbl(cls):
        cls.myDb.create_all()
