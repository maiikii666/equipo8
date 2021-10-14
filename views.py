from types import MethodDescriptorType
from flask import blueprints, render_template, request
from flask.helpers import flash, url_for
from werkzeug.utils import redirect
from forms import *

main= blueprints.Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def inicio():
    form = FormInicio()
    if (form.validate_on_submit()):
        usuario=request.form["usuario"]
        contrasena=request.form["contrasena"]
        if(usuario == "Estudiante"):
            return (informacionestudiante())
        if(usuario == "Profesor"):
            return (informacionprofesores())
        if(usuario == "Administrador"):
            return (adminRegistro())
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

@main.route("/creareditaractiv/", methods=["GET", "POST"])
def creareditaractiv():
    form = FormCrearActividad()
    if (form.validate_on_submit()):
        return ("ACTIVIDAD CREADA")
        ### Se debe actualizar la lista con las actividades, y salir alerta de actividad creada
    return render_template("creareditaractiv.html", form=form)

@main.route("/creareditaractivProfesor/", methods=["GET", "POST"])
def creareditaractivProfesor():
    form = FormCrearActividad()
    if (form.validate_on_submit()):
        return ("ACTIVIDAD CREADA")
        ###Debe retornar alerta de actividad creada
    return render_template("creareditaractivProfesor.html",)

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

@main.route("/informacionestudiante/", methods=["GET", "POST"])
def informacionestudiante():
    ### Si llega con GET muestra la información de la BD
    ### Si llega con POST actualiza la información en la BD
    form= FormActualizar()
    if (form.validate_on_submit()):
        return ("INFORMACIÓN ACTUALIZADA")
    formu= FormCambiarContrasena()
    if (formu.validate_on_submit()):
        return ("CONTRASEÑA CAMBIADA")
    return render_template("informacionestudiante.html", form=form, formu=formu)

@main.route("/informacionprofesores/", methods=["GET", "POST"])
def informacionprofesores():
    ### Si llega con GET muestra la información de la BD
    ### Si llega con POST actualiza la información en la BD
    form= FormActualizar()
    if (form.validate_on_submit()):
        return ("INFORMACIÓN ACTUALIZADA")
    formu= FormCambiarContrasena()
    if (formu.validate_on_submit()):
        return ("CONTRASEÑA CAMBIADA")
    return render_template("informacionprofesores.html", form=form, formu=formu)

@main.route("/notasestudiante/")
def notasestudiante():
    return render_template("notasestudiante.html")

@main.route("/retroalimentacionestudiante/")
def retroalimentacionestudiante():
    return render_template("retroalimentacionestudiante.html")