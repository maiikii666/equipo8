from flask import blueprints, render_template, request
from flask.helpers import flash, url_for
from werkzeug.utils import redirect
from forms import *

main= blueprints.Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def inicio():
    form = FormInicio()
    if (form.validate_on_submit()):
        return ("GRACIAS POR INICIAR SESION")
        ### Se dirige a la ventana de acuerdo al ROL
    return render_template("index.html", form=form)


@main.route("/adminAdministraMaterias/")
def adminAdministraMaterias():
###FALTA VISTA PARA AGREGAR ESTUDIANTE AL CURSO
    return render_template("adminAdministraMaterias.html")

@main.route("/administrarCursosProfesor/")
def administrarCursosProfesor():
    return render_template("administrarCursosProfesor.html")
    

@main.route("/adminRegistro/", methods=["GET", "POST"])
def adminRegistro():
    form = FormRegistrarUsuario()
    if (form.validate_on_submit()):
        return ("SE REGISTRO EL USUARIO")
        ### Regresa a la misma ventana con alerta, usuario registrado y lo almacena en la base de datos SQLITE
    return render_template("adminRegistro.html", form=form)

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

@main.route("/informacionestudiante/")
def informacionestudiante():
    return render_template("informacionestudiante.html")

@main.route("/informacionprofesores/")
def informacionprofesores():
    return render_template("informacionprofesores.html")

@main.route("/notasestudiante/")
def notasestudiante():
    return render_template("notasestudiante.html")

@main.route("/retroalimentacionestudiante/")
def retroalimentacionestudiante():
    return render_template("retroalimentacionestudiante.html")