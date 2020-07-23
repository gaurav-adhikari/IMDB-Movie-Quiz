"Forms Defination Modules "
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from quiz.Models import UserInfo


class LoginForm(FlaskForm):
    "Structures the Login Form"

    username = StringField('Username', validators=[
                           DataRequired(), Length(min=2, max=100)])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


class RegistrationForm(FlaskForm):

    "Structures the Registration Form"

    username = StringField('Username', validators=[
                           DataRequired(), Length(min=2, max=100)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=1, max=100)])
    confirmPassword = PasswordField(
        'Retype password', validators=[DataRequired(), EqualTo("password")])
    
    referralCode = StringField(
        'Enter your Referral Code', validators=[DataRequired(),Length(min=4,max=10)])
    
    submit = SubmitField("Register")
    

    def validate_username(self, username):
        "Checks and validates for the existing username while registration and raises an error when given username exists"

        user = UserInfo.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Sorry, the Username is already Taken")


    def validate_email(self, email):
        "Checks and validates for the existing email while registration and raises an error when given email exists"

        email = UserInfo.query.filter_by(email=email.data).first()
        if email:
                raise ValidationError("Sorry, the email is already Taken")


    def validate_referralCode(self,referralCode):
        "Checks and validates for the existing refferal while registration and raises an error when given referral code doesnt exist"

        referralCode = UserInfo.query.filter_by(referralCode=referralCode.data).first()==None
        if referralCode:
            raise ValidationError("Please enter a valid referral code")
