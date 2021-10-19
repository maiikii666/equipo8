from flask import jsonify, blueprints
from conn import conn, closeConn
from views import session



api = blueprints.Blueprint('api',__name__)


@api.route("/informacion/<string:rol>/<string:usuario>")
def informacion(rol, usuario):
    """Función que maneja la ruta de mensaje.

        Parameters:
        Ninguno

        Returns:
        Json con el contenido de la lista mensajes.
        """
    if rol == "Estudiante":
        rol = "alumnos"
    if rol == "Profesor":
        rol = "profesores"
    db = conn()
    query = "select * from "+rol+" where user = ?"
    usuarioConsulta=db.execute(query, (usuario,)).fetchone()
    
    db.commit()
    closeConn()

    usuarioJson = {}
    usuarioJson["codigo"] = usuarioConsulta[0]
    usuarioJson["nombre"] = usuarioConsulta[1]
    usuarioJson["apellido"] = usuarioConsulta[2]
    usuarioJson["correo"] = usuarioConsulta[3]
    usuarioJson["telefono"] = usuarioConsulta[4]
    usuarioJson["usuario"] = usuarioConsulta[5]

    return jsonify(usuarioJson)
