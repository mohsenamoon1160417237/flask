from memory_data.main import db, flask_app

with flask_app.app_context():
    db.create_all()
