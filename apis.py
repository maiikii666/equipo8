from sqlite3.dbapi2 import Error
from flask import json, jsonify, blueprints
from conn import conn, closeConn



api = blueprints.Blueprint('api',__name__)


@api.route("/informacion/<string:rol>/<string:usuario>")
def informacion(rol, usuario):

    if rol == "Estudiante":
        rol = "alumnos"
    if rol == "Profesor":
        rol = "profesores"
    
    try:
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
    except Error:
        print(Error)

@api.route("/listaEstudiantes/")
def listaEstudiantes():
    try:
        db = conn()
        query = "SELECT * from alumnos"
        resultadoConsulta = db.execute(query)
        estudiantes = resultadoConsulta.fetchall()
        db.commit()
        closeConn()


        estudiantesJson = []
        for estudiante in estudiantes:
            estudianteJson = {}
            estudianteJson["codigo"] = estudiante[0]
            estudianteJson["nombreYApellido"] = estudiante[1] + " " + estudiante[2]
            estudiantesJson.append(estudianteJson)

        return jsonify(estudiantesJson)

    except Error:
        print(Error)

#@api.route("/listaMatriculados/,<string:idMateria>")

@api.route("/materias/")
def listaMaterias():
    try:
        db = conn()
        query = "SELECT * from materias"
        resultadoConsulta = db.execute(query)
        materias = resultadoConsulta.fetchall()
        db.commit()
        closeConn()


        materiasJson = []
        for materia in materias:
            materiaJson = {}
            materiaJson["nombre"] = materia[1]
            materiaJson["profesor"] = materia[2]
            materiasJson.append(materiaJson)

        return jsonify(materiasJson)

    except Error:
        print(Error)

@api.route("/materias/<string:materia>/")
def seleccionarMateria(materia):
    try:
        db = conn()
        query = "SELECT * from materias where nombre_materia = ?"
        resultadoConsulta = db.execute(query, (materia,))
        materiaencontrada = resultadoConsulta.fetchone()
        query = "SELECT nombre_p, apellido_p from profesores where id_profesor = ?"
        profeABuscar = materiaencontrada[2]
        nombreProfe = db.execute(query, (profeABuscar,)).fetchone()
        query = "SELECT idAlumno from alumnosmaterias where nombreMateria = ?"
        alumnosMatriculados = db.execute(query, (materia,)).fetchall()
                
        alumnosMatriculadosJson = []
        for alumno in alumnosMatriculados:
            
            db = conn()
            query = "SELECT nombre, apellido from alumnos where id_alumno = ?"
            nombreAlumno = db.execute(query, (alumno[0],)).fetchone()
           
            query = "SELECT notafinal from alumnosmaterias where idAlumno = ? and nombreMateria = ?"
            nota = db.execute(query, (alumno[0], materia)).fetchone()
            alumnoJson = {}
            alumnoJson["codigo"] = alumno[0]
            alumnoJson["nombre"] = nombreAlumno[0]
            alumnoJson["apellido"] = nombreAlumno[1]
            alumnoJson["nota"] = nota[0]
            alumnosMatriculadosJson.append(alumnoJson)
        db.commit()
        closeConn()

        materiaJson = {}
        materiaJson["nombre"] = materiaencontrada[1]
        materiaJson["profesor"] = materiaencontrada[2]
        materiaJson["estudiantes"] = alumnosMatriculadosJson
        materiaJson["nombreProfe"] = nombreProfe[0] + " " + nombreProfe[1]

        return jsonify(materiaJson)
    except Error:
        print(Error)



@api.route("/materiasPorProfe/<string:usuario>/")
def seleccionarMateriasPorProfe(usuario):
    try:

        db = conn()
        query = "SELECT id_profesor from profesores where user = ?"
        usuarioPorId = db.execute(query, (usuario,)).fetchone()
        query = "SELECT * from materias where id_profesor = ?"
        resultadoConsulta = db.execute(query, (usuarioPorId[0],))
        materiasEncontradas = resultadoConsulta.fetchall()


        materiasJson = []
        for materia in materiasEncontradas:
            materiaJson = {}
            materiaJson["nombre"] = materia[1]
            materiaJson["profesor"] = materia[2]
            materiasJson.append(materiaJson)

        return jsonify(materiasJson)

    except Error:
        print(Error)



@api.route("/materiasYActividades/<string:materia>/")
def seleccionarMateriaYActividades(materia):
    try:
        db = conn()
        query = "SELECT * from materias where nombre_materia = ?"
        resultadoConsulta = db.execute(query, (materia,))
        materiaencontrada = resultadoConsulta.fetchone()
        query = "SELECT nombre_p, apellido_p from profesores where id_profesor = ?"
        profeABuscar = materiaencontrada[2]
        nombreProfe = db.execute(query, (profeABuscar,)).fetchone()

        db = conn()
        
        query = "SELECT * from actividades where nombreMateria = ?"
        actividades = db.execute(query, (materia,)).fetchall()
        actividadesJson = []
        for actividad in actividades:

            actividadJson = {}
            actividadJson["nombreActividad"] = actividad[1]
            actividadJson["descripcion"] = actividad[2]
            actividadesJson.append(actividadJson)
            
        db.commit()
        closeConn()

        materiaJson = {}
        materiaJson["nombre"] = materiaencontrada[1]
        materiaJson["profesor"] = materiaencontrada[2]
        materiaJson["actividades"] = actividadesJson
        materiaJson["nombreProfe"] = nombreProfe[0] + " " + nombreProfe[1]

        return jsonify(materiaJson)
    except Error:
        print(Error)
