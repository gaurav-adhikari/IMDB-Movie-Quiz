from flask import render_template, flash, redirect, url_for
from quiz import app,db,bcrypt
from quiz.forms import LoginForm, RegistrationForm
from quiz.Models import UserInfo
db.create_all()



@app.route("/", methods=["GET", "POST"])
def home():

    form = LoginForm()
    # Statc admin login
    if form.validate_on_submit():
        if form.username.data == "admin" and form.password.data == "admin":
            flash(" You have been Logged in ", "success")
            return redirect(url_for("dashboard"))
        else:
            flash(" Sorry you play quiz with these credentials", "danger")

    return render_template('home.html', form=form)

    

@app.route("/register", methods=["GET", "POST"])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():
        
        hashPassword=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        userRegistrationDetails = UserInfo(username=form.username.data,password=hashPassword,email=form.email.data)
        db.session.add(userRegistrationDetails)
        db.session.commit()

        flash("Registration succesful", "success")
        return redirect(url_for("home"))
    else:
        flash("Registration Failed", "danger")

    return render_template("registration.html", form=form)


@app.route("/dashboard",methods=["GET","POST"])
def dashboard():
    return render_template("dashboard.html")