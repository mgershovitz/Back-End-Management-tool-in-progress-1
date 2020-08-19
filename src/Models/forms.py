from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField, StringField, BooleanField
from wtforms.validators import DataRequired, Email, Length, NumberRange


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class RegisterNurseForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    name = StringField('Name',
                       validators=[DataRequired(), Length(min=2, max=20)], )
    id_num = StringField('Id Num',
                         validators=[DataRequired()])
    work_years = StringField('Work Years',
                             validators=[DataRequired()])
    employment_percentage = StringField('Employment Percentage',
                                        validators=[DataRequired()])
    courses = StringField('Courses',
                          validators=[DataRequired()])
    roles = StringField('Roles',
                        validators=[DataRequired()])
    submit = SubmitField('Register Nurse')
