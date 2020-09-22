from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField, StringField, BooleanField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()], )
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class RegisterNurseForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    nurse_license_id = StringField('Nurse Licence Id',
                         validators=[DataRequired()])
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


class InsertNewBirthData(FlaskForm):
    name = StringField('Name',
                       validators=[DataRequired(), Length(min=2, max=20)], )
    id_num = StringField('Id Num',
                         validators=[DataRequired()])
    pregnancy_week = StringField('Pregnancy Week',
                             validators=[DataRequired()])
    birth_number = StringField('Birth Number',
                                        validators=[DataRequired()])
    tolac = StringField('Tolac',
                          validators=[DataRequired()])
    estimated_weight = StringField('estimated_weight',
                        validators=[DataRequired()])
    induction_or_spontaneous = StringField('Induction or Spontaneous',
                         validators=[DataRequired()])
    fetal_lie = StringField('Fetal Lie',
                                           validators=[DataRequired()])
    epidural = StringField('Epidural',
                                           validators=[DataRequired()])
    submit = SubmitField('Insert birth data')
