from werkzeug.utils import validate_arguments, secure_filename
from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional

class FormInicio(Form):
    usuario = StringField("Usuario", validators=[DataRequired()])
    contrasena = PasswordField("Contrasena", validators=[DataRequired()])
    enviar = SubmitField("Iniciar Sesión")

class FormRegistrarUsuario(Form):
    nombre= StringField("Nombre", validators=[DataRequired()])
    apellido= StringField("Apellido", validators=[DataRequired()])
    codigo= StringField("Codigo", validators=[DataRequired()])
    telefono= StringField("Telefono", validators=[DataRequired()])
    correo= StringField("Correo", validators=[DataRequired()])
    rol= RadioField("Rol", choices=[("value","Estudiante"), ("value_two","Profesor")])
    usuario= StringField("Usuario", validators=[DataRequired()])
    contrasena = PasswordField("Contrasena", validators=[DataRequired()])
