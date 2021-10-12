from flask import blueprints, render_template, request

main= blueprints.Blueprint("main", __name__)

@main.route("/")
def inicio():
    return render_template("index.html")

@main.route("/adminAdministraMaterias/")
def adminAdministraMaterias():
    return render_template("adminAdministraMaterias.html")

@main.route("/administrarCursosProfesor/")
def administrarCursosProfesor():
    return render_template("administrarCursosProfesor.html")
    
@main.route("/adminRegistro/")
def adminRegistro():
    return render_template("adminRegistro.html")

@main.route("/busquedasadmin/")
def busquedasadmin():
    return render_template("busquedasadmin.html")

@main.route("/creareditaractiv/")
def creareditaractiv():
    return render_template("creareditaractiv.html")

@main.route("/creareditaractivProfesor/")
def creareditaractivProfesor():
    return render_template("creareditaractivProfesor.html")

@main.route("/crearMateria/")
def crearMateria():
    return render_template("crearMateria.html")

@main.route("/detalleactividadAdmin/")
def detalleactividadAdmin():
    return render_template("detalleactividadAdmin.html")

@main.route("/detalleActividadEstudiante/")
def detalleActividadEstudiante():
    return render_template("detalleActividadEstudiante.html")

@main.route("/detalleactividadProfesor/")
def detalleactividadProfesor():
    return render_template("detalleactividadProfesor.html")

@main.route("/informacionestudiante/")###ERROR EN LA IMAGEN FOTO USUARIO
def informacionestudiante():
    return render_template("informacionestudiante.html")

@main.route("/informacionprofesores/")###ERROR EN LA IMAGEN FOTO USUARIO
def informacionprofesores():
    return render_template("informacionprofesores.html")

@main.route("/notasestudiante/")
def notasestudiante():
    return render_template("notasestudiante.html")

@main.route("/retroalimentacionestudiante/")####ERROR EN LA IMAGEN DETALLES
def retroalimentacionestudiante():
    return render_template("retroalimentacionestudiante.html")