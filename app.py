from flask import Flask
import os

def create_app():
    app = Flask(__name__)


    app.secret_key= "surcoSistemaDeNotas" #os.urandom( 24 )
    from views import main
    from apis import api

    app.register_blueprint(main, url_prefix='/plataformaNotas')
    app.register_blueprint(api, url_prefix='/api')


    return app