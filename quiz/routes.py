from flask import render_template, flash, redirect, url_for,request
from quiz import app,db,bcrypt
from quiz.forms import LoginForm, RegistrationForm
from quiz.Models import UserInfo
from flask_login import login_user,current_user,logout_user,login_required
db.create_all()


@app.route("/", methods=["GET", "POST"])
def home():

    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))

    form = LoginForm()
    # Statc admin login
    if form.validate_on_submit():

        user=UserInfo.query.filter_by(username=form.username.data).first()
       
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user)
            loginPage = request.args.get("next")
            
            if loginPage:
                return redirect(loginPage)
            else:
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
@login_required
def dashboard():

    # if not current_user.is_authenticated:
    #     return redirect(url_for("home"))

    return render_template("dashboard.html")


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))