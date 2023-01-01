from main_app import flask_app
from models.memory_mdl import MemoryMdl

with flask_app.app_context():
    MemoryMdl.make_tbl()
