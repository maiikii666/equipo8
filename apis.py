from flask import jsonify, blueprints
from conn import conn, closeConn
from views import session



api = blueprints.Blueprint('api',__name__)


@api.route('/informacion/')
def informacion():
    """Función que maneja la ruta de mensaje.

        Parameters:
        Ninguno

        Returns:
        Json con el contenido de la lista mensajes.
        """
    


    """
    from mensaje import mensajes
    return jsonify(mensajes)
    """