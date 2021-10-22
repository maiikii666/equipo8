import functools
from sqlite3 import Error
from flask import blueprints, render_template, request, session, flash
from flask.helpers import flash, url_for
from werkzeug.utils import redirect
from forms import *
from conn import conn, closeConn
from werkzeug.security import check_password_hash, generate_password_hash

main= blueprints.Blueprint("main", __name__)

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if "usuario" not in session:
            return redirect(url_for("main.inicio"))
        return view(**kwargs)
    return wrapped_view

def login_estudiante(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if session["rol"] != "Estudiante":
            return redirect(url_for("main.inicio"))
        return view(**kwargs)
    return wrapped_view

def login_profesor(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if session["rol"] != "Profesor":
            return redirect(url_for("main.inicio"))
        return view(**kwargs)
    return wrapped_view

def login_administrador(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if session["rol"] != "Administrador":
            return redirect(url_for("main.inicio"))
        return view(**kwargs)
    return wrapped_view

@main.route("/", methods=["GET", "POST"])
def inicio():
    form = FormInicio()
    
    if (form.validate_on_submit()):
        usuario=request.form["usuario"]
        contrasena=request.form["contrasena"]
        db=conn()
        usuarioConsulta = db.execute("select * from login where user = ?", (usuario,)).fetchone()
        db.commit()

        if usuarioConsulta is not None:
            contrasena = contrasena + usuario + "Surcolombiana"
            sw = check_password_hash(usuarioConsulta[1], contrasena)        
            if(sw):
                if(usuarioConsulta[2] == "Estudiante"):
                    session["usuario"]=usuarioConsulta[0]
                    session["rol"]=usuarioConsulta[2]
                    closeConn()
                    return (notasestudiante())
                if(usuarioConsulta[2] == "Profesor"):
                    session["usuario"]=usuarioConsulta[0]
                    session["rol"]=usuarioConsulta[2]
                    closeConn()
                    return (administrarCursosProfesor())
                if(usuarioConsulta[2] == "Administrador"):
                    session["usuario"]=usuarioConsulta[0]
                    session["rol"]=usuarioConsulta[2]
                    closeConn()
                    return (busquedasadmin())
            else:
                flash("Contraseña incorrecta")
        if usuarioConsulta is None:
            flash("Usuario incorrecto")

    return render_template("index.html", form=form)



@main.route("/adminAdministraMaterias/", methods=["GET", "POST"])
@login_required
@login_administrador
def adminAdministraMaterias(): ### AQUÍ VOY

    formularioAgregarEstudiante = FormAgregarEstudiantesCrearMateria()
    formularioRemoverEstudiante = FormRemoverEstudiantesCrearMateria()




    return render_template("adminAdministraMaterias.html", formularioAgregarEstudiante=formularioAgregarEstudiante, formularioRemoverEstudiante=formularioRemoverEstudiante)


@main.route("/administrarCursosProfesor/")
@login_required
@login_profesor
def administrarCursosProfesor():
    return render_template("administrarCursosProfesor.html")
    

@main.route("/adminRegistro/", methods=["GET", "POST"])
@login_required
@login_administrador
def adminRegistro():
    form = FormRegistrarUsuario()
    if (form.validate_on_submit()):
        nombre= request.form["nombre"]
        apellido= request.form["apellido"]
        codigo= request.form["codigo"]
        telefono= request.form["telefono"]
        correo= request.form["correo"]
        rol= request.form["rol"]
        usuario= request.form["usuario"]
        contrasena= request.form["contrasena"]
        contrasena= contrasena + usuario + "Surcolombiana"
        contrasena = generate_password_hash(contrasena)

        valoresAIngresar=(usuario,contrasena,rol)
        query="insert into login(user, password, rol)values(?,?,?)"
        try:
            db = conn()
            db.execute(query, valoresAIngresar)
            db.commit()
            print("Usuario Ingresado a login")
            
        except Error:
            print(Error)    
        
        if (rol == "Estudiante"):
            try:
                valoresAIngresar=(codigo, nombre, apellido, correo, telefono, usuario)
                query="insert into alumnos(id_alumno,nombre,apellido,correo,telefono,user)values(?,?,?,?,?,?)"
                db.execute(query, valoresAIngresar)
                db.commit()
                print("Usuario Ingresado a alumnos")
                closeConn()
            except Error:
                print(Error)
        
        if (rol == "Profesor"):
            try:
                valoresAIngresar=(codigo, nombre, apellido, correo, telefono, usuario)
                query="insert into profesores(id_profesor,nombre_p,apellido_p,correo_p,telefono_p,user)values(?,?,?,?,?,?)"
                print(query, valoresAIngresar)
                db.execute(query, valoresAIngresar)
                db.commit()
                print("Usuario Ingresado a profesor")
                closeConn()
            except Error:
                print(Error)
    return render_template("adminRegistro.html", form=form)


@main.route("/busquedasadmin/")
@login_required
@login_administrador
def busquedasadmin():
    return render_template("busquedasadmin.html")


@main.route("/creareditaractiv/", methods=["GET", "POST"])
@login_required
@login_administrador
def creareditaractiv():
    form = FormCrearActividad()
    if (form.validate_on_submit()):
        return ("ACTIVIDAD CREADA")
        ### Se debe actualizar la lista con las actividades, y salir alerta de actividad creada
    return render_template("creareditaractiv.html", form=form)


@main.route("/creareditaractivProfesor/", methods=["GET", "POST"])
@login_required
@login_profesor
def creareditaractivProfesor():
    form = FormCrearActividad()
    if (form.validate_on_submit()):
        return ("ACTIVIDAD CREADA")
        ###Debe retornar alerta de actividad creada
    return render_template("creareditaractivProfesor.html",)


@main.route("/crearMateria/", methods=["GET", "POST"])
@login_required
@login_administrador
def crearMateria():
    formularioCrearMateria = FormCrearMateria()
    if (formularioCrearMateria.validate_on_submit()):
        nombreMateria = request.form["nombreMateria"]
        profesorMateria= request.form["profesorMateria"]
        query="INSERT into materias(nombre_materia,id_profesor) VALUES(?,?);" 
        valoresAIngresar=(nombreMateria,profesorMateria)

        try:
            db = conn()
            db.execute(query, valoresAIngresar)
            db.commit()
        except Error:
            print(Error)
    return render_template("crearMateria.html",  formularioCrearMateria=formularioCrearMateria)


@main.route("/detalleactividadAdmin/")
@login_required
@login_administrador
def detalleactividadAdmin():
    return render_template("detalleactividadAdmin.html")


@main.route("/detalleActividadEstudiante/")
@login_required
@login_estudiante
def detalleActividadEstudiante():
    return render_template("detalleActividadEstudiante.html")


@main.route("/detalleactividadProfesor/")
@login_required
@login_profesor
def detalleactividadProfesor():
    return render_template("detalleactividadProfesor.html")


@main.route("/informacionestudiante/", methods=["GET", "POST"])
@login_required
@login_estudiante
def informacionestudiante():
    flash(session["usuario"])
    form= FormActualizar()
    if (form.validate_on_submit()):
        telefonoNuevo=request.form["telefono"]
        correoNuevo=request.form["correo"]
        usuarioActual=session["usuario"]
        query="update alumnos set telefono = ?, correo = ? where user = ?"
        valoresACambiar = (telefonoNuevo, correoNuevo, usuarioActual)
        print(query,valoresACambiar)
        try:
            db = conn()
            db.execute(query, valoresACambiar)
            db.commit()
            closeConn()
        except Error:
            print(Error)

    formu= FormCambiarContrasena()
    if (formu.validate_on_submit()):
        return ("CONTRASEÑA CAMBIADA")
    return render_template("informacionestudiante.html", form=form, formu=formu)


@main.route("/informacionprofesores/", methods=["GET", "POST"])
@login_required
@login_profesor
def informacionprofesores():
    flash(session["usuario"])
    form= FormActualizar()
    if (form.validate_on_submit()):
        telefonoNuevo=request.form["telefono"]
        correoNuevo=request.form["correo"]
        usuarioActual=session["usuario"]
        query="update profesores set telefono_p = ?, correo_p = ? where user = ?"
        valoresACambiar = (telefonoNuevo, correoNuevo, usuarioActual)
        print(query,valoresACambiar)
        try:
            db = conn()
            db.execute(query, valoresACambiar)
            db.commit()
            closeConn()
        except Error:
            print(Error)

    formu= FormCambiarContrasena()
    if (formu.validate_on_submit()):
        return ("CONTRASEÑA CAMBIADA")
    return render_template("informacionprofesores.html", form=form, formu=formu)


@main.route("/notasestudiante/")
@login_required
@login_estudiante
def notasestudiante():
    return render_template("notasestudiante.html")


@main.route("/retroalimentacionestudiante/")
@login_required
@login_estudiante
def retroalimentacionestudiante():
    return render_template("retroalimentacionestudiante.html")


@main.route("/salir/")
@login_required
def salir():
    session.clear()
    return redirect(url_for("main.inicio"))
