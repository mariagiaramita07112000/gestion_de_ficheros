from movements import app
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from flask import render_template

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired("debes introducir el correo")])
    password = PasswordField('Password', validators=[DataRequired("debes introducir tu contraseña")])
    submit = SubmitField('Sign In')