from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError
from wtforms.validators import DataRequired,Email,EqualTo

from ..models import User

class RegistrationForm(FlaskForm):
    
    username = StringField("username",validators=[DataRequired()])
    email = StringField("email",validators=[DataRequired(),Email()])
    password = PasswordField("password",validators=[DataRequired(),EqualTo('password_confirm',message='Passwords do not match')])
    password_confirm = PasswordField("confirm password",validators=[DataRequired()])
    submit = SubmitField('Sign Up')


    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError("Email is already in use")

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username already exists')


class LoginForm(FlaskForm):
    username =  StringField('',validators=[DataRequired()])
    password = PasswordField('',validators=[DataRequired()])
    submit = SubmitField('Sign In')
