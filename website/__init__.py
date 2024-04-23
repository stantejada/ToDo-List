from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918"
    return app
