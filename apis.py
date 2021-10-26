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

            query = "SELECT id_actividad from actividades where nombreMateria = ?"
            dataActividades = db.execute(query, (materia,)).fetchall()
            totalActividades = len(dataActividades)
            total = 0
            
            for actividad in dataActividades:
                query = "SELECT nota from actividadesPorAlumnos where idAlumno = ? and idActividad = ?"
                notasActividades = db.execute(query, (alumno[0],actividad[0])).fetchall()

                for nota in notasActividades:
                    total += float(nota[0])
            if (totalActividades != 0):
                notaFinal = total/totalActividades    

                query = "update alumnosmaterias set notaFinal = ? where idAlumno = ?"
                db.execute(query, (notaFinal, alumno[0]))
                db.commit

                alumnoJson["nota"] = notaFinal
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
            actividadJson["id"] = actividad[0]
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



@api.route("/actividad/<string:actividad>/")
def buscarActividad(actividad):
    try:
        db = conn()
        query = "SELECT * from actividades where id_actividad = ?"
        dataActividad = db.execute(query, (actividad,)).fetchone()
        materiaActividad = dataActividad[3]
        query = "select idAlumno from alumnosmaterias where nombreMateria = ?"
        estudiantesQuePresentan = db.execute(query, (materiaActividad,)).fetchall()
        actividadJson = {}
        actividadJson["nombre"] = dataActividad[1]
        actividadJson["descripcion"] = dataActividad[2]
        actividadJson["materia"] = materiaActividad
        estudiantesJson = []
        

        for estudiante in estudiantesQuePresentan:
            estudianteJson = {}
            estudianteJson["codigo"] = estudiante[0]
            
            query = "select * from actividadesPorAlumnos where idActividad = ? and idAlumno = ?"
            infoActividadEstudiante = db.execute(query, (actividad,estudiante[0])).fetchone()
            if infoActividadEstudiante == None:
                print("Vacio")
                estudianteJson["nota"] = "Por calificar"
            else:
                estudianteJson["nota"] = infoActividadEstudiante[2]

            estudiantesJson.append(estudianteJson)

        actividadJson["estudiantes"] = estudiantesJson

        return jsonify(actividadJson)
    except Error:
        print(Error)




@api.route("/notasEstudiante/<string:usuarioAlumno>/")
def notasEstudiante(usuarioAlumno):
    try:
        db = conn()
        query = "select id_alumno from alumnos where user = ?"
        infoAlumno = db.execute(query,(usuarioAlumno,)).fetchone()
        idAlumno = infoAlumno[0]

        notasAlumnoJson = {}

        notasDeMaterias = []

        notasDeActividades = []

        query = "select * from alumnosmaterias where idAlumno = ?"
        infoMateriasPorAlumno = db.execute(query,(idAlumno,)).fetchall()
        for materia in infoMateriasPorAlumno:
            materiaJson = {}
            materiaJson["nombre"] = materia[0]
            materiaJson["nota"] = materia[2]
            notasDeMaterias.append(materiaJson)

        query = "select * from actividadesPorAlumnos where idAlumno = ?"
        infoActividadesALumno = db.execute(query, (idAlumno,)).fetchall()

        for actividad in infoActividadesALumno:
            actividadJson = {}
            actividadJson["id"] = actividad[1]
            actividadJson["nota"] = actividad[2]
            actividadJson["retroalimentacion"] = actividad[3]
            query = "select * from actividades where id_actividad = ?"
            infoactividadPorId = db.execute(query, (actividad[1],)).fetchone()
            actividadJson["nombre"] = infoactividadPorId[1]
            actividadJson["descripcion"] = infoactividadPorId[2]
            actividadJson["materia"] = infoactividadPorId[3]
            notasDeActividades.append(actividadJson)
        
        notasAlumnoJson["materias"] =notasDeMaterias
        notasAlumnoJson["actividades"] = notasDeActividades

        promedioFinal=0
        if notasAlumnoJson["materias"] != None:
            totalnota=0
            for materia in notasAlumnoJson["materias"]:
                totalnota += float(materia["nota"])
                promedioFinal = totalnota/len(notasAlumnoJson["materias"])
        notasAlumnoJson["promedioFinal"] = promedioFinal


        return jsonify(notasAlumnoJson)

    except Error:
        print(Error)