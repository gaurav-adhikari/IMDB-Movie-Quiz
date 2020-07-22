from flask import render_template, flash, redirect, url_for, request
from quiz import app, db, bcrypt
from quiz.forms import LoginForm, RegistrationForm
from quiz.Models import UserInfo,Questions
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy import desc
db.create_all()



@app.route("/", methods=["GET", "POST"])
def home():

    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))

    form = LoginForm()
    # Statc admin login
    if form.validate_on_submit():

        user = UserInfo.query.filter_by(username=form.username.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            loginPage = request.args.get("next")

            if loginPage:
                return redirect(loginPage)
            else:
                return redirect(url_for("dashboard"))
        else:
            flash(" Sorry you cannot play quiz with these credentials", "danger")

    return render_template('home.html', form=form)


@app.route("/register", methods=["GET", "POST"])
def register():

    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))

    form = RegistrationForm()

    if form.validate_on_submit():
        hashPassword = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        userRegistrationDetails = UserInfo(
            username=form.username.data, password=hashPassword, email=form.email.data)
        db.session.add(userRegistrationDetails)
        db.session.commit()

        flash("Registration succesful", "success")
        return redirect(url_for("home"))

    return render_template("registration.html", form=form)


@app.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():

    maxScore = db.session.query(db.func.max(UserInfo.recentScore)).scalar()
    page = request.args.get("page", 1, type=int)
    allUserDatas = UserInfo.query.order_by(
        desc(UserInfo.recentScore)).paginate(page=page, per_page=3)
    return render_template("dashboard.html", userDatas=allUserDatas, currentUser=current_user.username, maxScore=maxScore)


@app.route("/takeQuiz",methods=["GET","POST"])
@login_required
def takeQuiz():

    currentUser= current_user
    questions=Questions.query.all()
    return render_template("quizExam.html",recentScore=currentUser.recentScore,username=currentUser.username,questions=questions)

@app.route("/logout")
def logout():

    logout_user()
    return redirect(url_for("home"))
