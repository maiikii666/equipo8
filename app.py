from flask import Flask
import os

def create_app():
    app = Flask(__name__)


    app.secret_key=os.urandom( 24 )
    from views import main
    app.register_blueprint(main)

    return app