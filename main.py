from main_app import flask_app
from routes.api_memory import api_memory

if __name__ == "__main__":
    flask_app.register_blueprint(api_memory)
    flask_app.run(debug=True)
