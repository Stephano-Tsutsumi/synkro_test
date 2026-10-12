DEBUG = True

def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = DEBUG
    return app
