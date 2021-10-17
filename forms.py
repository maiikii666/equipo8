from werkzeug.utils import validate_arguments, secure_filename
from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, RadioField
from wtforms.fields.html5 import EmailField
from wtforms.fields.core import DateField
from wtforms.validators import DataRequired, InputRequired, Email

class FormInicio(Form):
    usuario = StringField("Usuario", validators=[InputRequired()])
    contrasena = PasswordField("Contrasena", validators=[InputRequired()])
    enviar = SubmitField("Iniciar Sesión")

class FormRegistrarUsuario(Form):
    nombre= StringField("Nombre", validators=[DataRequired()])
    apellido= StringField("Apellido", validators=[DataRequired()])
    codigo= StringField("Codigo", validators=[DataRequired()])
    telefono= StringField("Telefono", validators=[DataRequired()])
    correo= EmailField("Correo", validators=[DataRequired(), Email(message=None, granular_message=False, check_deliverability=False, allow_smtputf8=True, allow_empty_local=False)])
    rol= RadioField("Rol", choices=[("Estudiante"), ("Profesor")])
    usuario= StringField("Usuario", validators=[DataRequired()])
    contrasena = PasswordField("Contrasena", validators=[DataRequired()])
    crear= SubmitField("Crear")

class FormCrearActividad(Form):
    nombreActividad= StringField("Nombre", validators=[DataRequired()])
    fechaDeInicio= DateField("Inicio", validators=[DataRequired()])
    fechaDeCierre= DateField("Cierre", validators=[DataRequired()])
    descripcion= StringField("Descripción", validators=[DataRequired()])
    enviar= SubmitField("Guardar")

class FormActualizar(Form):
    nombre= StringField("Nombre", validators=[DataRequired()])
    apellido= StringField("Apellido", validators=[DataRequired()])
    telefono= StringField("Telefono", validators=[DataRequired()])
    correo= StringField("Correo", validators=[DataRequired()])
    guardar= SubmitField("Guardar")

class FormCambiarContrasena(Form):
    contrasena= PasswordField("Contraseña", validators=[DataRequired()])
    contrasenaNueva= PasswordField("Contraseña", validators=[DataRequired()])
    contrasenaConfirmada= PasswordField("Contraseña", validators=[DataRequired()])
    cambiar= SubmitField("Cambiar Contraseña")