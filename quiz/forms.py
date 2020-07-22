
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from quiz.Models import UserInfo


class LoginForm(FlaskForm):

    username = StringField('Username', validators=[
                           DataRequired(), Length(min=2, max=100)])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=2, max=100)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=1, max=100)])
    confirmPassword = PasswordField(
        'Retype password', validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Register")


class ChoiceForm(FlaskForm):
    choiceField=RadioField(label="",choices=[],validators=[DataRequired()])


def validate_username(self, username):
    user = UserInfo.query.filter_by(username=username.data).first()
    if user:
        raise ValidationError("Sorry the Username is already Taken")


def validate_email(self, email):
    email = UserInfo.query.filter_by(email=email.data).first()
    if email:
            raise ValidationError("Sorry the email is already Taken")
