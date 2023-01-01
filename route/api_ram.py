from flask import request
from flask_sqlalchemy import SQLAlchemy

from memory_data import flask_app
from views.RamCtrl import RamCtrl


@flask_app.route('/getRamInfo')
def getRamInfo():
    n = request.args.get('n')
    db = SQLAlchemy(flask_app)
    ramCtrl = RamCtrl(db)
    return ramCtrl.getRamInfo(n)

