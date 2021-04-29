# Importacion de modulos

import os
from flask import Flask

def create_app():
    app = Flask(__name__)


    app.config.from_mapping(

        SECRET_KEY='mikey',
        DATABASE_HOST=os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_PASSSWORD=os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE_USER=os.environ.get('FLASK_DATABASE_USER'),
        DATABASE=os.environ.get('FLASK_DATABASE'),
    )

    # Ruta de prueba

    @app.route('/hola')
    def hola():
        return 'Prueba de desarrollo'

    return app
