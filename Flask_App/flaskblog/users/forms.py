from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, PasswordField, SubmitField, BooleanField, RadioField, TextField
from wtforms.fields.html5 import TelField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    email2 = StringField('Email Address 2', validators=[DataRequired(), Email()])
    gender = RadioField('Gender', choices=[('male', 'Male'), ('female', 'Female')])
    name = TextField('First Name', validators=[DataRequired()])
    surname = TextField('Surname', validators=[DataRequired()])
    # date = DateField('Date', format='%m/%d/%Y',validators=[DataRequired()])
    home_number1 = TelField('Home Number', validators=[DataRequired()])
    home_number2 = TelField('Home Number 2', validators=[DataRequired()])
    cell_phone = TelField('Cell Phone Number', validators=[DataRequired()])
    cellphone_number2 = TelField('Alternative Cellphone Number', validators=[DataRequired()])
    guardian_cell1 = TelField('Parent/Guardian Number', validators=[DataRequired()])
    accountholder_cell= TelField('Account Holder Cellphone Number', validators=[DataRequired()])
    work_daytime_number = TelField('Work/Daytime Number', validators=[DataRequired()])
    guardian_cell2 = TelField('Alternative Parent/Guardian Number', validators=[DataRequired()])
    next_of_kin = TextField('Next of Kin', validators=[DataRequired()])
    next_of_kin_number = TelField('Next of Kin Number', validators=[DataRequired()])
    medical_dental_history = TextField('Medical Dental History', validators=[DataRequired()])
    medical_aid_details = TextField('Medical Aid Details', validators=[DataRequired()])
    dependent_number = TelField('Dependent Number', validators=[DataRequired()])
    postal_address = TextField('Postal Address', validators=[DataRequired()])
    physical_address = TextField('Physical Address', validators=[DataRequired()])
    insurance_type = TextField('Insurance Type', validators=[DataRequired()])
    employer = TextField('Employer', validators=[DataRequired()])
    occupation = TextField('Occupation', validators=[DataRequired()])
    surname_and_initials = TextField('Surname & Initials', validators=[DataRequired()])
    identity_number2 = TelField('Identification Number', validators=[DataRequired()])
    doctor = TextField('Current Doctor', validators=[DataRequired()])
    alternative_doctor = TextField('Alternative Doctor', validators=[DataRequired()])
    identity_number = TelField ('Identification Number', validators=[DataRequired()])
    language = TextField('Preffered Language', validators=[DataRequired()])
    attending_school = TextField('Attending School')
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    terms_acceptance = RadioField('Terms Acceptance', choices=[('yes', 'Accept')])
    liabilty_acceptance = RadioField('Liability Acceptance', choices=[('yes', 'Accept')])

    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    name = TextField('First Name', validators=[DataRequired()])
    surname = TextField('Surname', validators=[DataRequired()])
    email2 = StringField('Email Address 2', validators=[DataRequired(), Email()])
    # date = DateField('Date', format='%m/%d/%Y',validators=[DataRequired()])
    home_number1 = TelField('Home Number', validators=[DataRequired()])
    home_number2 = TelField('Home Number 2', validators=[DataRequired()])
    cell_phone = TelField('Cell Phone Number', validators=[DataRequired()])
    cellphone_number2 = TelField('Alternative Cellphone Number', validators=[DataRequired()])
    guardian_cell1 = TelField('Parent/Guardian Number', validators=[DataRequired()])
    accountholder_cell= TelField('Account Holder Cellphone Number', validators=[DataRequired()])
    work_daytime_number = TelField('Work/Daytime Number', validators=[DataRequired()])
    guardian_cell2 = TelField('Alternative Parent/Guardian Number', validators=[DataRequired()])
    next_of_kin = TextField('Next of Kin', validators=[DataRequired()])
    next_of_kin_number = TelField('Next of Kin Number', validators=[DataRequired()])
    medical_dental_history = TextField('Medical Dental History', validators=[DataRequired()])
    medical_aid_details = TextField('Medical Aid Details', validators=[DataRequired()])
    dependent_number = TelField('Dependent Number', validators=[DataRequired()])
    postal_address = TextField('Postal Address', validators=[DataRequired()])
    physical_address = TextField('Physical Address', validators=[DataRequired()])
    insurance_type = TextField('Insurance Type', validators=[DataRequired()])
    employer = TextField('Employer', validators=[DataRequired()])
    occupation = TextField('Occupation', validators=[DataRequired()])
    surname_and_initials = TextField('Surname & Initials', validators=[DataRequired()])
    identity_number2 = TelField('Identification Number', validators=[DataRequired()])
    doctor = TextField('Current Doctor', validators=[DataRequired()])
    alternative_doctor = TextField('Alternative Doctor', validators=[DataRequired()])
    identity_number = TelField ('Identification Number', validators=[DataRequired()])
    language = TextField('Preffered Language', validators=[DataRequired()])
    attending_school = TextField('Attending School')
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')


    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')

    def validate_email2(self, email2):
        if email2.data != current_user.email2:
            user = User.query.filter_by(email2=email2.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')

class RequestResetForm(FlaskForm):
    email = StringField('Email',
    validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email. You must register first.')

class ResetPasswordForm(FlaskForm):
        password = PasswordField('Password', validators=[DataRequired()])
        confirm_password = PasswordField('Confirm Password',
                                         validators=[DataRequired(), EqualTo('password')])
        submit = SubmitField('Reset Password')
